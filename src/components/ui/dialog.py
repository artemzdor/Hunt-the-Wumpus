from uuid import UUID
from dataclasses import dataclass, field
from typing import List, Tuple, Type, Any, Dict, Set

from src.systems.base import System
from src.components.base import Component


@dataclass
class ComponentDialogEvent(Component):
    commands: Set[str] = field(
        default_factory=set, metadata="Команды взаимодействия"
    )
    systems: List[Type[System]] = field(
        default_factory=list, metadata="Системы которым передается событие"
    )
    kwargs: Dict[str, Any] = field(
        default_factory=dict, metadata="Аргументы"
    )
    enet_type: str = field(
        default="", metadata="Тип события"
    )
    next_dialog: UUID = field(default=..., metadata="Следующий диалог")


@dataclass
class ComponentDialog(Component):
    renderings: List[Tuple[Type[System], UUID]] = field(
        default_factory=list, metadata="Системы рендерига диалогов"
    )
    dialogs: List[ComponentDialogEvent] = field(
        default_factory=list, metadata="Диалоги(клавиша, система, значение)"
    )
