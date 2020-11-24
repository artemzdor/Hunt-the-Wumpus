from uuid import UUID
from typing import Any, Dict, List, Optional, Tuple

from src.core.scene import Scene
from src.systems.base import System
from src.components.base import Component
from src.systems.word.word import SystemWord
from src.systems.ui.render import SystemRender
from src.components.ui.dialog import ComponentDialogEvent
from src.components.world.position import ComponentPosition


class SystemMove(SystemRender):

    def process(self, scene: Scene):
        pass

    def _event_input(self, value: Tuple[int, int], scene: Scene, entity_id: UUID,
                     value_name: str, component: ComponentPosition) -> bool:
        if value_name == "coordinate_x_y":
            system_word: Optional[SystemWord] = scene.get_system(SystemWord)

            if system_word is None:
                return False

            move: bool = system_word.set_move(
                entity_id=entity_id,
                component=component,
                move_x=value[0],
                move_y=value[1]
            )
            return move

    def event(self, scene: Scene, system_event: System, event_type: str, entity_id: UUID,
              component: Component, value: Any, value_name: str, kwargs: Dict[str, Any]) -> None:
        if event_type == "input":
            self._event_input(value_name=value_name, value=value,
                              component=component, scene=scene, entity_id=entity_id)

    def _get_move_points(self, position: ComponentPosition) -> List[Tuple[int, int, str, str]]:
        """Получаем кординаты для передвижения без проверки"""
        points: List[Tuple[int, int, str, str]] = list()  # x, y, command, display_info
        x: int = position.x
        y: int = position.y
        for speed in range(1, position.speed + 1):
            points.append((x - speed, y, "a", "Влево идти"))
            points.append((x + speed, y, "d", "Вправо идти"))
            points.append((x, y - speed, "s", "Вниз идти"))
            points.append((x, y + speed, "w", "Вверх идти"))
        return points

    def get_move_points(self, system_word: SystemWord,
                        position: ComponentPosition) -> List[Tuple[int, int, str, str]]:
        """Получаем кординаты для передвижения"""
        points: List[Tuple[int, int, str, str]] = list()
        for x, y, command, display_info in self._get_move_points(position=position):
            if system_word.is_move(x=x, y=y):
                points.append((x, y, command, display_info))
        return points

    def _render(self, system_word: SystemWord, position: ComponentPosition,
                entity_id: UUID, next_dialog: UUID) -> List[ComponentDialogEvent]:
        events: List[ComponentDialogEvent] = list()
        for x, y, command, display_info in self.get_move_points(position=position, system_word=system_word):
            event: ComponentDialogEvent = ComponentDialogEvent(
                command=command,
                display_info=display_info,
                system_type=SystemMove,
                kwargs={},
                value=(x, y),
                value_name="coordinate_x_y",
                entity_id=entity_id,
                component_type=ComponentPosition,
                next_dialog=next_dialog
            )
            events.append(event)
        return events

    def render(self, scene: Scene, render_entity_id: UUID, next_dialog: UUID) -> List[ComponentDialogEvent]:

        system_word: Optional[SystemWord] = scene.get_system(SystemWord)
        position: Optional[ComponentPosition] = scene.get_component(
            entity_id=render_entity_id, component=ComponentPosition
        )

        if system_word is None or position is None:
            return []

        events: List[ComponentDialogEvent] = self._render(
            system_word=system_word,
            position=position,
            entity_id=render_entity_id,
            next_dialog=next_dialog
        )
        scene.set_resource("dialog", next_dialog)
        return events
