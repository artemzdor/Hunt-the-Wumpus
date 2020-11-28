from uuid import UUID
from dataclasses import dataclass, field
from typing import List, Type, Any, Dict

from src.systems.base import System
from src.components.base import Component


@dataclass
class ComponentDialogEvent(Component):
    command: str = field(
        default=..., metadata="Команды взаимодействия"
    )
    info: bool = field(
        default=False, metadata="признак информации"
    )
    display_info: str = field(
        default=..., metadata="Описание команды"
    )
    system_type: Type[System] = field(
        default_factory=list, metadata="Система которой передается событие"
    )
    kwargs: Dict[str, Any] = field(
        default_factory=dict, metadata="Аргументы"
    )
    value: Any = field(
        default=..., metadata="Значения события"
    )
    value_name: str = field(
        default=..., metadata="Имя изменяемого значения"
    )
    entity_id: UUID = field(
        default=..., metadata="Куда передаются значения"
    )
    component_type: Type[Component] = field(
        default=..., metadata="Изменяемый компонет"
    )
    next_dialog: UUID = field(default=..., metadata="Следующий диалог")


@dataclass
class ComponentDialogRender(Component):
    system_type: Type[System] = field(
        default=..., metadata="Система генерируемая события"
    )
    entity_id: UUID = field(
        default=..., metadata="Куда передаются значения"
    )
    component: Type[Component] = field(
        default=..., metadata="Изменяемый компонет"
    )
    next_dialog: UUID = field(default=..., metadata="Следующий диалог")


@dataclass
class ComponentDialog(Component):
    renderings: List[ComponentDialogRender] = field(
        default_factory=list, metadata="Системы рендерига диалогов"
    )
    dialog_events: List[ComponentDialogEvent] = field(
        default_factory=list, metadata="Диалоги"
    )
