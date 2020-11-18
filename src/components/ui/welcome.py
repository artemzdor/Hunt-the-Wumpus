from dataclasses import dataclass, field

from src.components.base import Component


@dataclass
class ComponentWelcome(Component):
    welcome_text: str = field(
        default="Привет ты попал в удивительный мир приключений",
        metadata="Экран приветсвия"
    )
