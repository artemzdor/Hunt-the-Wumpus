from uuid import UUID
from typing import List
from dataclasses import dataclass, field

from src.components.base import Component


@dataclass
class ComponentInventory(Component):
    items: List[UUID] = field(
        default_factory=list, metadata="Список предметов"
    )
    entity_item: UUID = field(
        default=..., metadata="Id для рендеринга списка предметов"
    )
    next_dialog: UUID = field(
        default=..., metadata="Следующий диалог"
    )
