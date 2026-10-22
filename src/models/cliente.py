from dataclasses import dataclass
from typing import Optional


@dataclass
class Cliente:
    """Representa um cliente da loja Constrular."""

    id_cliente: Optional[int]
    nome: str
    cpf: Optional[str] = None
    telefone: Optional[str] = None
    email: Optional[str] = None
    cidade: Optional[str] = None
    estado: Optional[str] = None

    @classmethod
    def from_row(cls, row):
        """Cria um Cliente a partir de uma linha retornada pelo banco."""
        return cls(
            id_cliente=row[0],
            nome=row[1],
            cpf=row[2],
            telefone=row[3],
            email=row[4],
            cidade=row[5],
            estado=row[6],
        )
