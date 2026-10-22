from dataclasses import dataclass
from typing import Optional


@dataclass
class Fornecedor:
    """Representa um fornecedor de produtos."""

    id_fornecedor: Optional[int]
    nome: str
    telefone: Optional[str] = None
    email: Optional[str] = None
    cidade: Optional[str] = None
    estado: Optional[str] = None

    @classmethod
    def from_row(cls, row):
        """Cria um Fornecedor a partir de uma linha retornada pelo banco."""
        return cls(
            id_fornecedor=row[0],
            nome=row[1],
            telefone=row[2],
            email=row[3],
            cidade=row[4],
            estado=row[5],
        )
