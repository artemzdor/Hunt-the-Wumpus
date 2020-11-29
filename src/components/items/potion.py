from dataclasses import dataclass, field

from src.components.base import Component


@dataclass
class ComponentPotion(Component):
    """Компонент баночка востановления"""
    hp: int = field(
        default=..., metadata="Сколько очков жизней для востановления"
    )

