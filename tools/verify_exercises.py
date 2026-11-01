#!/usr/bin/env python3
"""Verifica se os exercícios continuam idênticos ao manifesto SHA-256.

Uso:
    python3 tools/verify_exercises.py

O script apenas lê os arquivos. Ele não executa, não reescreve e não
corrige nenhum exercício.
"""

from __future__ import annotations

import hashlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs" / "EXERCISE-MANIFEST.sha256"
CHAPTER_PATTERN = "0[1-7]-*"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_manifest(path: Path = MANIFEST) -> dict[str, str]:
    entries: dict[str, str] = {}
    if not path.exists():
        raise FileNotFoundError(f"Manifesto não encontrado: {path}")

    for number, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if "  " not in line:
            raise ValueError(f"Linha {number} inválida no manifesto: {line!r}")
        digest, relative = line.split("  ", 1)
        if len(digest) != 64:
            raise ValueError(f"Hash inválido na linha {number}: {digest!r}")
        entries[relative] = digest.lower()
    return entries


def chapter_files(root: Path = ROOT) -> dict[str, Path]:
    files: dict[str, Path] = {}
    for directory in sorted(root.glob(CHAPTER_PATTERN)):
        if not directory.is_dir():
            continue
        for path in sorted(directory.rglob("*.py")):
            if path.is_file():
                files[path.relative_to(root).as_posix()] = path
    return files


def verify(root: Path = ROOT, manifest: Path = MANIFEST) -> dict[str, list[str]]:
    expected = load_manifest(manifest)
    actual = chapter_files(root)

    missing = sorted(set(expected) - set(actual))
    extra = sorted(set(actual) - set(expected))
    changed = sorted(
        relative
        for relative, digest in expected.items()
        if relative in actual and sha256(actual[relative]) != digest
    )

    return {
        "missing": missing,
        "extra": extra,
        "changed": changed,
        "expected": sorted(expected),
    }


def main() -> int:
    try:
        result = verify()
    except (FileNotFoundError, ValueError) as error:
        print(f"ERRO: {error}", file=sys.stderr)
        return 1

    expected = result["expected"]
    problems = result["missing"] + result["extra"] + result["changed"]
    print(f"Exercícios no manifesto: {len(expected)}")

    if not problems:
        print("Integridade: OK — todos os exercícios estão idênticos ao manifesto.")
        return 0

    if result["missing"]:
        print("\nArquivos do manifesto que não existem mais:")
        for relative in result["missing"]:
            print(f"  - {relative}")

    if result["extra"]:
        print("\nArquivos novos que não estão no manifesto:")
        for relative in result["extra"]:
            print(f"  - {relative}")

    if result["changed"]:
        print("\nArquivos modificados:")
        for relative in result["changed"]:
            print(f"  - {relative}")

    print("\nIntegridade: FALHOU. Nenhum exercício deve ser alterado sem revisão.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
