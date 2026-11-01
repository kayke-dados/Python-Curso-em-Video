"""Testes das verificações do repositório."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.dont_write_bytecode = True

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import check_repository as repository  # noqa: E402
import verify_exercises  # noqa: E402


class SlugTests(unittest.TestCase):
    def test_acentos_sao_preservados(self) -> None:
        self.assertEqual(repository.slugify("Exercícios"), "exercícios")
        self.assertEqual(repository.slugify("Apresentação"), "apresentação")

    def test_espacos_viram_hifens(self) -> None:
        self.assertEqual(repository.slugify("Como executar"), "como-executar")
        self.assertEqual(repository.slugify("Tabela de exercícios"), "tabela-de-exercícios")


class TableTests(unittest.TestCase):
    def test_extrai_nomes_da_primeira_coluna(self) -> None:
        text = "\n".join(
            [
                "| Arquivo | Conceito |",
                "|---|---|",
                "| `01 - Olá.py` | saída |",
                "| 02 - Soma.py | contas |",
            ]
        )
        self.assertEqual(
            repository.extract_table_filenames(text),
            {"01 - Olá.py", "02 - Soma.py"},
        )


class ManifestTests(unittest.TestCase):
    def test_manifesto_tem_87_exercicios(self) -> None:
        self.assertEqual(len(verify_exercises.load_manifest()), 87)

    def test_nenhum_exercicio_mudou(self) -> None:
        result = verify_exercises.verify()
        self.assertEqual(result["missing"], [])
        self.assertEqual(result["extra"], [])
        self.assertEqual(result["changed"], [])


class RepositoryTests(unittest.TestCase):
    def test_sintaxe(self) -> None:
        self.assertEqual(repository.check_syntax(), [])

    def test_contagens_do_readme(self) -> None:
        self.assertEqual(repository.check_counts(), [])

    def test_tabelas_dos_capitulos(self) -> None:
        self.assertEqual(repository.check_chapter_tables(), [])

    def test_links_internos(self) -> None:
        errors, _external = repository.check_links()
        self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()
