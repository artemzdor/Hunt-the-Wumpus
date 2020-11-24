from uuid import UUID
from typing import Dict, Any, List

from src.core.scene import Scene
from src.systems.base import System
from src.components.base import Component
from src.systems.ui.render import SystemRender
from src.components.ui.dialog import ComponentDialogEvent


class SystemExit(SystemRender):

    def process(self, scene: Scene):
        pass

    def event(self, scene: Scene, system_event: System, event_type: str, entity_id: UUID,
              component: Component, value: Any,  value_name: str, kwargs: Dict[str, Any]) -> None:
        exit()

    def render(self, scene: Scene, render_entity_id: UUID, next_dialog: UUID) -> List[ComponentDialogEvent]:
        event_y: ComponentDialogEvent = ComponentDialogEvent(
            command="qq",
            display_info="Выход",
            system_type=SystemExit,
            kwargs={},
            value=True,
            value_name="",
            entity_id=render_entity_id,
            component_type=type(None),
            next_dialog=next_dialog,
        )
        scene.set_resource("dialog", render_entity_id)
        return [event_y]
