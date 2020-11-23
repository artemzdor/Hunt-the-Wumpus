from uuid import UUID
from typing import List

from src.core.scene import Scene
from src.systems.base import System
from src.components.ui.dialog import ComponentDialogEvent


class SystemRender(System):

    def render(
        self, scene: Scene, render_entity_id: UUID
    ) -> List[ComponentDialogEvent]:
        """Метод создания ComponentDialogEvent"""
        return []
