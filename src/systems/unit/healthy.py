from uuid import UUID
from typing import Tuple, Type

from src.core.scene import Scene
from src.systems.base import System
from src.components.base import Component
from src.components.unit.healthy import (
    ComponentUnitHealthy
)


class SystemUnitHealthy(System):

    def process(self, scene: Scene):
        pass

    def _add_healthy(self, component: ComponentUnitHealthy, healthy: int) -> None:
        """Добовление жизней"""
        component.healthy += healthy

        healthy_max: int = component.healthy_max

        if healthy_max != component.healthy:
            component.healthy %= healthy_max + 1

    def _deprive_healthy(self, component_healthy: ComponentUnitHealthy,
                         component_game_status: Component, healthy: int) -> None:
        """Отнятие жизней, убить юнита"""
        if component_healthy.healthy <= healthy:
            if component_healthy.revival > 1:
                component_healthy.revival -= 1
                self._add_healthy(component_healthy, component_healthy.healthy_max)
            else:
                # TODO: персонаж умирает component_game_status
                pass
        else:
            component_healthy.healthy -= healthy

    def add_healthy(
            self, healthy: int, entity_id: UUID, scene: Scene
    ) -> bool:
        """Добоаляем жизни"""
        if component := scene.get_component(entity_id, ComponentUnitHealthy):
            self._add_healthy(component=component, healthy=healthy)
            return True
        return False

    def deprive_healthy(
            self, healthy: int, entity_id: UUID, scene: Scene
    ) -> bool:
        """Отымаем жизни"""
        type_components: Tuple[Type[Component], ...] = (
            ComponentUnitHealthy
        )

        if components := scene.get_components(entity_id, type_components):
            self._deprive_healthy(
                component_healthy=components[ComponentUnitHealthy],
                healthy=healthy,
                component_game_status=Component(), #  TODO: Компонент убийства юнита
            )
            return True
        return False
