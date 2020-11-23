import os
import subprocess
from uuid import UUID
from typing import List, Optional

from src.core.scene import Scene
from src.systems.base import System
from src.systems.ui.render import SystemRender
from src.systems.ui.display import SystemDisplay
from src.components.ui.dialog import (
    ComponentDialog,
    ComponentDialogEvent,
    ComponentDialogRender
)
from src.systems.ui.system_input import SystemInput


class SystemDialog(System):

    def process(self, scene: Scene):
        pass

    def clear(self) -> None:
        """Очистка Экрана"""
        if os.name == 'posix':
            subprocess.call("clear", shell=True)
        elif os.name in ('ce', 'nt', 'dos'):
            subprocess.call("cls", shell=True)

    def _get_dialogs(
            self, scene: Scene, component: ComponentDialog
    ) -> List[ComponentDialogEvent]:
        """Получение диалогов"""
        renderings: List[ComponentDialogEvent] = list()
        for render_iter in component.renderings:
            render_iter: ComponentDialogRender
            system: Optional[SystemRender] = scene.get_system(
                render_iter.system_type
            )
            for render in system.render(scene, render_iter.entity_id):
                render: ComponentDialogEvent
                renderings.append(render)
        return renderings

    def _dialog(self, scene: Scene, entity_id: UUID) -> bool:
        """Генерация диалогов"""
        if component := scene.get_component(entity_id, ComponentDialog):
            component: ComponentDialog
            component.dialog_events = self._get_dialogs(scene, component)
            return True
        return False

    def _show_display(self, scene: Scene, entity_id: UUID) -> bool:
        """Отрисовка диалогов"""
        system_display: Optional[SystemDisplay] = scene.get_system(SystemDisplay)
        system_input: Optional[SystemInput] = scene.get_system(SystemInput)

        component_dialog: Optional[ComponentDialog] = scene.get_component(
            entity_id=entity_id, component=ComponentDialog)

        if system_display is None or system_input is None or component_dialog is None:
            return False

        self.clear()
        system_display.display_print(scene=scene, component_dialog=component_dialog)
        component_dialog = scene.get_component(entity_id=entity_id, component=ComponentDialog)
        system_input.display_input(scene=scene, component_dialog=component_dialog)

        return True

    def dialog(self, scene: Scene, entity_id: UUID) -> None:
        """Отрисовка диалогов"""
        dialog: bool = self._dialog(scene, entity_id)
        if dialog:
            display: bool = self._show_display(scene, entity_id)
            if not display:
                raise RuntimeError("Не удалось отрендерить")
