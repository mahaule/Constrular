from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class ItemVenda:
    """Representa um item (produto) dentro de uma venda."""

    id_item: Optional[int]
    venda_id: int
    produto_id: int
    quantidade: int
    preco_unitario: float

    def __post_init__(self):
        if self.quantidade is not None and self.quantidade <= 0:
            raise ValueError("A quantidade deve ser maior que zero.")
        if self.preco_unitario is not None and self.preco_unitario < 0:
            raise ValueError("O preço unitário não pode ser negativo.")

    @property
    def subtotal(self):
        return round(self.quantidade * self.preco_unitario, 2)


@dataclass
class Venda:
    """Representa uma venda realizada na loja."""

    id_venda: Optional[int]
    data_venda: Optional[str]
    cliente_id: int
    funcionario_id: int
    forma_pagamento: str
    itens: List[ItemVenda] = field(default_factory=list)

    @property
    def total(self):
        return round(sum(item.subtotal for item in self.itens), 2)

    @classmethod
    def from_row(cls, row):
        """Cria uma Venda a partir de uma linha resumida retornada pelo banco."""
        return cls(
            id_venda=row[0],
            data_venda=row[1],
            cliente_id=row[2],
            funcionario_id=row[3],
            forma_pagamento=row[4],
        )
