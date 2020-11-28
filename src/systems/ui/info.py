from uuid import UUID
from typing import Any, Dict, List, Optional

from src.core.scene import Scene
from src.entities.base import Entity
from src.systems.base import System
from src.components.base import Component
from src.systems.ui.render import SystemRender
from src.components.ui.dialog import ComponentDialogEvent
from src.components.world.position import ComponentPosition
from src.components.unit.healthy import ComponentUnitHealthy


class SystemInfo(SystemRender):
    # информация персонажа
    player: Entity

    def __init__(self, player: Entity):
        self.player = player

    def process(self, scene: Scene):
        pass

    def event(self, scene: Scene, system_event: System, event_type: str, entity_id: UUID,
              component: Component, value: Any,  value_name: str, kwargs: Dict[str, Any]) -> None:
        exit()

    def get_health(self, scene: Scene) -> str:
        """Информация о текущем состояние жизней"""
        if health := self.player.get_component(ComponentUnitHealthy):
            health: ComponentUnitHealthy
            return f"Hp: {health.healthy}"

    def get_position(self, scene: Scene) -> Optional[str]:
        """Информация о текущей позиции персонажа"""
        if position := self.player.get_component(ComponentPosition):
            position: ComponentPosition
            return f"Position: (x: {position.x}, y: {position.y})"

    def get_display_info(self, scene: Scene) -> str:
        template: List[Optional[str]] = [
            self.get_health(scene=scene),
            self.get_position(scene=scene)
        ]
        render: str = " | ".join(i for i in template if i)
        return f"{render}"

    def render(self, scene: Scene, render_entity_id: UUID, next_dialog: UUID) -> List[ComponentDialogEvent]:
        event: ComponentDialogEvent = ComponentDialogEvent(
            command="",
            display_info=self.get_display_info(scene=scene),
            system_type=System,
            kwargs={},
            value=None,
            value_name="",
            entity_id=render_entity_id,
            component_type=type(None),
            next_dialog=next_dialog,
            info=True,
        )
        return [event]
