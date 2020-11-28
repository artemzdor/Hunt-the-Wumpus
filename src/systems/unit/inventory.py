from uuid import UUID
from typing import Dict, Any, List

from src.core.default import GameStatus
from src.core.scene import Scene
from src.entities.base import Entity
from src.systems.base import System
from src.components.base import Component
from src.systems.ui.render import SystemRender
from src.components.ui.dialog import ComponentDialogEvent, ComponentDialogRender
from src.components.unit.inventory import ComponentInventory


class SystemInventory(SystemRender):

    def process(self, scene: Scene):
        pass

    def event(self, scene: Scene, system_event: System, event_type: str, entity_id: UUID,
              component: Component, value: Any, value_name: str, kwargs: Dict[str, Any]) -> None:
        component: ComponentInventory
        scene.set_resource("dialog", component.entity_item)
        scene.set_status(GameStatus.dialog)

    def render(self, scene: Scene, render_entity_id: UUID, next_dialog: UUID) -> List[ComponentDialogEvent]:
        event: ComponentDialogEvent = ComponentDialogEvent(
            command="i",
            display_info="Инвентарь",
            system_type=SystemInventory,
            value=None,
            value_name="",
            entity_id=render_entity_id,
            component_type=ComponentInventory,
            next_dialog=next_dialog,
        )
        scene.set_resource("dialog", render_entity_id)
        return [event]
