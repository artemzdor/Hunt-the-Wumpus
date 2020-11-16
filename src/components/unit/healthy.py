from dataclasses import dataclass, field

from src.components.base import Component


@dataclass
class ComponentUnitHealthy(Component):
    healthy: int = field(
        metadata="Начальное количество жизней"
    )
    healthy_max: int = field(
        metadata="Максимальное количество жизней"
    )
    revival: int = field(
        metadata="Количество возрождений"
    )
