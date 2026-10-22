from dataclasses import dataclass
from typing import Optional


@dataclass
class Funcionario:
    """Representa um funcionário da loja Constrular."""

    id_funcionario: Optional[int]
    nome: str
    cargo: Optional[str] = None
    salario: float = 0.0
    telefone: Optional[str] = None

    def __post_init__(self):
        if self.salario is not None and self.salario < 0:
            raise ValueError("O salário não pode ser negativo.")

    @classmethod
    def from_row(cls, row):
        """Cria um Funcionario a partir de uma linha retornada pelo banco."""
        return cls(
            id_funcionario=row[0],
            nome=row[1],
            cargo=row[2],
            salario=float(row[3]) if row[3] is not None else 0.0,
            telefone=row[4],
        )
