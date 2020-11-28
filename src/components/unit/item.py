from typing import Type
from dataclasses import dataclass, field

from src.systems.base import System
from src.components.base import Component


@dataclass
class ComponentItem(Component):
    name: str = field(
        default=..., metadata="Имя предмета"
    )
    system_type: Type[System] = field(
        default=..., metadata="Система для работы с предметом"
    )
