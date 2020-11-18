from typing import List
from dataclasses import dataclass, field

from src.entities.base import Entity
from src.components.base import Component


@dataclass
class ComponentCoordinates(Component):
    word: List[List[List[Entity]]] = field(
        default_factory=list, metadata="Кординатная сетка местности"
    )

    width: int = field(default=..., metadata="Ширина мира (X)")
    height: int = field(default=..., metadata="Высота мира (Y)")
