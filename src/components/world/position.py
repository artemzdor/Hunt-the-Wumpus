from dataclasses import dataclass, field

from src.components.base import Component


@dataclass
class ComponentPosition(Component):
    x: int = field(metadata="Кордината X (Ширина)")
    y: int = field(metadata="Кордината Y (Высота)")
