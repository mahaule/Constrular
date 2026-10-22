from dataclasses import dataclass
from typing import Optional


@dataclass
class Produto:
    """Representa um produto do catálogo da loja."""

    id_produto: Optional[int]
    nome: str
    descricao: Optional[str] = None
    preco_custo: float = 0.0
    preco_venda: float = 0.0
    estoque_minimo: int = 0
    categoria_id: Optional[int] = None
    fornecedor_id: Optional[int] = None

    def __post_init__(self):
        if self.preco_custo is not None and self.preco_custo < 0:
            raise ValueError("O preço de custo não pode ser negativo.")
        if self.preco_venda is not None and self.preco_venda < 0:
            raise ValueError("O preço de venda não pode ser negativo.")

    @property
    def margem_lucro(self):
        """Retorna a margem de lucro em reais (venda - custo)."""
        return round(self.preco_venda - self.preco_custo, 2)

    @classmethod
    def from_row(cls, row):
        """Cria um Produto a partir de uma linha completa retornada pelo banco."""
        return cls(
            id_produto=row[0],
            nome=row[1],
            descricao=row[2],
            preco_custo=float(row[3]),
            preco_venda=float(row[4]),
            estoque_minimo=row[5],
            categoria_id=row[6],
            fornecedor_id=row[7],
        )
