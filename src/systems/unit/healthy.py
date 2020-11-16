from uuid import UUID
from typing import Optional

from src.core.scene import Scene
from src.systems.base import System
from src.components.unit.healthy import ComponentUnitHealthy


class SystemUnitHealthy(System):

    def process(self, scene: Scene):
        pass

    @classmethod
    def add_healthy(
            cls, healthy: int, entity_id: UUID, scene: Scene
    ) -> bool:
        component_healthy: Optional[ComponentUnitHealthy]
        component_healthy = scene.get_component(
            entity_id=entity_id, component=ComponentUnitHealthy
        )

        if healthy is None:
            return False

        component_healthy.healthy += healthy

        healthy_max: int = component_healthy.healthy_max

        if healthy_max != component_healthy.healthy:
            component_healthy.healthy %= healthy_max + 1

        return True
