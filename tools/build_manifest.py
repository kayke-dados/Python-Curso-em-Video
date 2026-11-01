#!/usr/bin/env python3
"""Gera o manifesto SHA-256 dos exercícios.

Uso:
    python3 tools/build_manifest.py           # mostra o que seria gravado
    python3 tools/build_manifest.py --write   # grava docs/EXERCISE-MANIFEST.sha256

Use --write somente ao adicionar exercícios novos. Exercícios existentes
não devem ser reescritos para "fazer o manifesto passar".
"""

from __future__ import annotations

import sys

sys.dont_write_bytecode = True

from verify_exercises import MANIFEST, ROOT, chapter_files, sha256


def build_lines() -> list[str]:
    return [
        f"{sha256(path)}  {relative}"
        for relative, path in sorted(chapter_files(ROOT).items())
    ]


def main(argv: list[str]) -> int:
    invalid = [arg for arg in argv if arg != "--write"]
    if invalid:
        print(f"Argumento desconhecido: {invalid[0]}", file=sys.stderr)
        return 2

    lines = build_lines()
    if "--write" not in argv:
        print(f"{len(lines)} exercícios encontrados. Nada foi gravado.")
        print("Use --write para atualizar o manifesto.")
        return 0

    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Manifesto atualizado com {len(lines)} exercícios: {MANIFEST}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
