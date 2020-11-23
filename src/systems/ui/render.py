import os
import subprocess
from typing import Type, Tuple, List
from uuid import UUID

from src.core.scene import Scene
from src.systems.base import System
from src.components.ui.dialog import ComponentDialogEvent


class SystemRender(System):

    def render(
        self, scene: Scene, render_entity_id: UUID
    ) -> List[ComponentDialogEvent]:
        return []
