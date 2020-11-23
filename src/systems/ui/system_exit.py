from typing import Dict, Any, List
from uuid import UUID

from src.components.ui.dialog import ComponentDialogEvent
from src.core.scene import Scene
from src.systems.base import System
from src.components.base import Component
from src.systems.ui.render import SystemRender


class SystemExit(SystemRender):

    def process(self, scene: Scene):
        pass

    def event(self, scene: Scene, system_event: System, event_type: str,
              component: Component, value: Any,  value_name: str, kwargs: Dict[str, Any]):
        exit()

    def render(self, scene: Scene, render_entity_id: UUID) -> List[ComponentDialogEvent]:
        event: ComponentDialogEvent = ComponentDialogEvent(
            command="q",
            display_info="Выход",
            system_type=SystemExit,
            kwargs={},
            value=None,
            value_name="",
            entity_id=render_entity_id,
            component_type=type(None),
            next_dialog=render_entity_id
        )
        return [event]
