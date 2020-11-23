from uuid import UUID

from src.core.scene import Scene
from src.systems.base import System
from src.components.ui.dialog import ComponentDialogEvent, ComponentDialog, ComponentDialogRender


class SystemDisplay(System):

    def process(self, scene: Scene):
        pass

    def _get_text(self, component: ComponentDialogEvent) -> str:
        return f"{component.command} - {component.display_info}"

    def _display_print(self, text: str) -> None:
        print(text)

    def display_print(self, scene: Scene, component_dialog: ComponentDialog) -> None:
        for component_render in component_dialog.dialog_events:
            component_render: ComponentDialogEvent
            text: str = self._get_text(component=component_render)
            self._display_print(text=text)
