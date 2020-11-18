from uuid import UUID
from typing import Dict, Type, Optional, Tuple
from dataclasses import dataclass, field

from src.components.base import Component
from src.systems.base import System
from src.entities.base import Entity


@dataclass
class Scene:
    entities: Dict[UUID, Entity] = field(
        default_factory=dict, metadata="Игровые обьекты"
    )
    systems: Dict[Type[System], System] = field(
        default_factory=dict, metadata="Системы игрового мира"
    )

    def get_system(self, system: Type[System]) -> Optional[System]:
        return self.systems.get(system)

    def get_entity(self, entity_id: UUID) -> Optional[Entity]:
        return self.entities.get(entity_id)

    def get_component(self, entity_id: UUID, component: Type[Component]) -> Optional[Component]:
        entity: Optional[Entity] = self.get_entity(entity_id=entity_id)
        if entity is not None:
            return entity.get_component(component)

    def get_components(
            self, entity_id: UUID, components: Tuple[Type[Component], ...]
    ) -> Optional[Dict[Type[Component], Component]]:
        """Возвращает все компоненты или ни одного"""
        if len(components) == 0:
            return

        components_map: Dict[Type[Component], Component] = dict()
        if entity := self.get_entity(entity_id=entity_id):
            for component_type in components:
                if component := entity.get_component(component_type):
                    components_map[component_type] = component
                else:
                    return

        if len(components) == len(components_map):
            return components_map
