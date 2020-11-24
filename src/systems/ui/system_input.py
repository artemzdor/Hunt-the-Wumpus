from uuid import UUID
from typing import List, Any, Dict, Optional

from src.core.scene import Scene
from src.systems.base import System
from src.components.base import Component
from src.components.ui.dialog import (
    ComponentDialogEvent,
    ComponentDialog
)


class SystemInput(System):

    def process(self, scene: Scene):
        pass

    def _event_system(
            self, system: Optional[System], component: Optional[Component], value: Any, entity_id: UUID,
            scene: Scene, value_name: str, kwargs: Dict[str, Any], event_type: str = "input"
    ) -> bool:
        """Передача события системе"""
        if system is None:
            return False
        system.event(scene=scene, system_event=system, component=component, entity_id=entity_id,
                     value=value, value_name=value_name, kwargs=kwargs, event_type=event_type)

    def display_input(self, scene: Scene, component_dialog: ComponentDialog) -> bool:
        """Получени ввода"""
        try:
            input_text: str = input("Введите вариант: ").strip()
        except UnicodeDecodeError:
            return False

        events: List[ComponentDialogEvent]

        for component in component_dialog.dialog_events:
            if component.command == input_text:
                system: Optional[System] = scene.get_system(component.system_type)
                component_input: Optional[Component] = scene.get_component(
                    entity_id=component.entity_id,
                    component=component.component_type
                )
                value: Any = component.value
                value_name: str = component.value_name
                kwargs: Dict[str, Any] = component.kwargs
                entity_id: UUID = component.entity_id

                event_result: bool = self._event_system(
                    system=system,
                    component=component_input,
                    value=value,
                    value_name=value_name,
                    kwargs=kwargs,
                    scene=scene,
                    entity_id=entity_id
                )
                return event_result

        return False
