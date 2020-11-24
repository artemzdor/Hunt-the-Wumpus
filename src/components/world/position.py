from dataclasses import dataclass, field

from src.components.base import Component


@dataclass
class ComponentPosition(Component):
    x: int = field(default=..., metadata="Кордината X (Ширина)")
    y: int = field(default=..., metadata="Кордината Y (Высота)")
    speed: int = field(default=1, metadata="Скорость передвижения")
