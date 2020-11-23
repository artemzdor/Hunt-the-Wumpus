from src.core.scene import Scene
from src.systems.base import System
from src.components.ui.dialog import (
    ComponentDialogEvent,
    ComponentDialog
)


class SystemDisplay(System):

    def process(self, scene: Scene):
        pass

    def _get_text(self, component: ComponentDialogEvent) -> str:
        """Получение текста для отрисовки"""
        if component.command and component.display_info:
            return f"{component.command} <- {component.display_info}"
        else:
            return f"{component.display_info}"

    def _display_print(self, text: str) -> None:
        """Отрисовка Диалога"""
        print(text)

    def display_print(self, scene: Scene, component_dialog: ComponentDialog) -> None:
        """Отрисовка всех диалогов"""
        for component_render in component_dialog.dialog_events:
            component_render: ComponentDialogEvent
            text: str = self._get_text(component=component_render)
            self._display_print(text=text)
