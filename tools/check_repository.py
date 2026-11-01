#!/usr/bin/env python3
"""Verificações do Python-Journey sem executar os exercícios.

Checa sintaxe, integridade dos arquivos, contagens do README, tabelas dos
capítulos, links internos e arquivos desnecessários.

Uso:
    python3 tools/check_repository.py
    python3 tools/check_repository.py --external
"""

from __future__ import annotations

import argparse
import ast
import re
import sys
import unicodedata
from pathlib import Path
from urllib.parse import unquote
from urllib.request import Request, urlopen

sys.dont_write_bytecode = True

from verify_exercises import ROOT, chapter_files, verify

DOCS = ROOT / "docs"
SKIP_DIRS = {".git", ".planning", ".venv", "venv", "node_modules"}
TRAVERSAL_SKIP = {".git", ".planning", ".venv", "venv", "node_modules", "__pycache__"}
LINK_PATTERN = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
IMAGE_PATTERN = re.compile(r"<img[^>]+src=\"([^\"]+)\"")
TABLE_ROW = re.compile(r"^\|\s*([^|]+?)\s*\|")
README_COUNT = re.compile(r"^\|\s*(\d{2})\s*—[^|]*\|\s*(\d+)\s*\|", re.M)


def slugify(text: str) -> str:
    """Aproxima o slug de título usado pelo GitHub."""
    text = text.strip().lower()
    text = "".join(
        char
        for char in unicodedata.normalize("NFKC", text)
        if char.isalnum() or char in {" ", "-", "_"} or unicodedata.category(char).startswith("L")
    )
    return re.sub(r"\s+", "-", text).strip("-")


def markdown_headings(path: Path) -> set[str]:
    headings: set[str] = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        match = re.match(r"^#{1,6}\s+(.+?)\s*$", line)
        if match:
            headings.add(slugify(match.group(1)))
    return headings


def markdown_files() -> list[Path]:
    files = [ROOT / "README.md", ROOT / "AUDIT.md", ROOT / "CHANGELOG.md", ROOT / "CONTRIBUTING.md"]
    files.extend(sorted(DOCS.rglob("*.md")))
    extra = ROOT / "07-proximos-aprendizados" / "README.md"
    if extra.exists():
        files.append(extra)
    return [path for path in files if path.exists()]


def extract_table_filenames(text: str) -> set[str]:
    names: set[str] = set()
    for line in text.splitlines():
        match = TABLE_ROW.match(line)
        if not match:
            continue
        cell = match.group(1).strip().strip("`")
        if not cell or cell == "Arquivo" or cell.startswith("---"):
            continue
        names.add(cell)
    return names


def check_syntax() -> list[str]:
    errors: list[str] = []
    for path in sorted(ROOT.rglob("*.py")):
        if any(part in TRAVERSAL_SKIP for part in path.parts):
            continue
        try:
            ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        except (SyntaxError, UnicodeDecodeError) as error:
            errors.append(f"Sintaxe: {path.relative_to(ROOT)}: {error}")
    return errors


def check_integrity() -> list[str]:
    result = verify()
    errors: list[str] = []
    for key, message in (
        ("missing", "removido"),
        ("extra", "novo e fora do manifesto"),
        ("changed", "modificado"),
    ):
        for relative in result[key]:
            errors.append(f"Exercício {message}: {relative}")
    return errors


def check_counts() -> list[str]:
    errors: list[str] = []
    actual = chapter_files(ROOT)
    counts: dict[str, int] = {}
    for relative in actual:
        counts[relative.split("/", 1)[0]] = counts.get(relative.split("/", 1)[0], 0) + 1

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    found = README_COUNT.findall(readme)
    if not found:
        errors.append("Contagens: nenhuma tabela de capítulos encontrada no README.")

    for number, raw_count in found:
        prefix = f"{number}-"
        folder = next((name for name in counts if name.startswith(prefix)), None)
        if folder is None:
            errors.append(f"Contagens: capítulo {number} não existe no repositório.")
            continue
        if counts[folder] != int(raw_count):
            errors.append(
                f"Contagens: capítulo {number} tem {counts[folder]} arquivos, "
                f"mas o README informa {raw_count}."
            )

    if "87 de 87" not in readme:
        errors.append("Contagens: o README não informa 87 de 87 exercícios.")

    for stale in ("86 de 86", "85/86", "9/10", "ex105 pendente"):
        if stale in readme:
            errors.append(f"Contagem antiga encontrada no README: {stale}")

    return errors


def check_chapter_tables() -> list[str]:
    errors: list[str] = []
    for doc in sorted((DOCS / "capitulos").glob("*.md")):
        if doc.stem.startswith("07-"):
            continue
        folder = ROOT / doc.stem
        if not folder.is_dir():
            errors.append(f"Capítulo sem pasta: {doc.name} -> {folder.name}")
            continue

        documented = extract_table_filenames(doc.read_text(encoding="utf-8"))
        actual = {path.name for path in folder.rglob("*.py")}
        missing = sorted(actual - documented)
        extra = sorted(documented - actual)

        for name in missing:
            errors.append(f"Tabela de {doc.stem}: exercício não documentado: {name}")
        for name in extra:
            errors.append(f"Tabela de {doc.stem}: nome que não existe na pasta: {name}")

    return errors


def check_links() -> tuple[list[str], list[str]]:
    errors: list[str] = []
    external: list[str] = []

    for path in markdown_files():
        text = path.read_text(encoding="utf-8")
        targets = LINK_PATTERN.findall(text) + IMAGE_PATTERN.findall(text)
        for raw in targets:
            target = raw.strip()
            if not target:
                continue
            if target.startswith(("http://", "https://", "mailto:", "tel:")):
                if target.startswith(("http://", "https://")):
                    external.append(target)
                continue

            file_part, _, anchor = target.partition("#")
            file_part = unquote(file_part)
            destination = path if not file_part else (path.parent / file_part).resolve()
            if not destination.exists():
                errors.append(f"Link quebrado em {path.relative_to(ROOT)}: {target}")
                continue

            if anchor and destination.suffix == ".md":
                if slugify(unquote(anchor)) not in markdown_headings(destination):
                    errors.append(
                        f"Âncora não encontrada em {path.relative_to(ROOT)}: {target}"
                    )

    return errors, sorted(set(external))


def check_external_links(urls: list[str]) -> list[str]:
    errors: list[str] = []
    for url in urls:
        request = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        try:
            with urlopen(request, timeout=20) as response:
                if response.status >= 400:
                    errors.append(f"Link externo retornou {response.status}: {url}")
        except Exception as error:  # noqa: BLE001 - relatório simples
            errors.append(f"Link externo inacessível: {url} ({error})")
    return errors


def check_unnecessary() -> list[str]:
    warnings: list[str] = []
    for path in sorted(ROOT.rglob("*")):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        name = path.name
        if name in {".DS_Store", "Thumbs.db"} or name.endswith((".swp", ".pyc", ".pyo", ".output")):
            warnings.append(f"Arquivo desnecessário: {path.relative_to(ROOT)}")
    return warnings


def main() -> int:
    parser = argparse.ArgumentParser(description="Verifica o repositório sem executar exercícios.")
    parser.add_argument("--external", action="store_true", help="também verifica links externos")
    args = parser.parse_args()

    print("Verificando sintaxe...")
    syntax_errors = check_syntax()
    print("Verificando integridade dos exercícios...")
    integrity_errors = check_integrity()
    print("Verificando contagens do README...")
    count_errors = check_counts()
    print("Verificando tabelas dos capítulos...")
    table_errors = check_chapter_tables()
    print("Verificando links internos...")
    link_errors, external = check_links()
    print("Verificando arquivos desnecessários...")
    warnings = check_unnecessary()

    external_errors: list[str] = []
    if args.external:
        print(f"Verificando {len(external)} links externos...")
        external_errors = check_external_links(external)

    errors = syntax_errors + integrity_errors + count_errors + table_errors + link_errors + external_errors

    print()
    print(f"Sintaxe: {'OK' if not syntax_errors else 'FALHOU'}")
    print(f"Integridade: {'OK' if not integrity_errors else 'FALHOU'}")
    print(f"Contagens: {'OK' if not count_errors else 'FALHOU'}")
    print(f"Tabelas: {'OK' if not table_errors else 'FALHOU'}")
    print(f"Links internos: {'OK' if not link_errors else 'FALHOU'} ({len(external)} externos)")
    if args.external:
        print(f"Links externos: {'OK' if not external_errors else 'FALHOU'}")
    if warnings:
        print(f"Avisos: {len(warnings)}")
        for warning in warnings:
            print(f"  - {warning}")

    if errors:
        print(f"\n{len(errors)} problema(s):")
        for error in errors:
            print(f"  - {error}")
        return 1

    print("\nTudo certo.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
