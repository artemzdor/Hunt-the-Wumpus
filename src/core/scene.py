from uuid import UUID
from dataclasses import dataclass, field
from typing import Dict, Type, Optional, Tuple, Any

from src.systems.base import System
from src.entities.base import Entity
from src.core.default import GameStatus
from src.components.base import Component
from src.entities.world.world import new_world
from src.entities.ui.dialog import new_base_dialog



@dataclass
class Scene:
    entities: Dict[UUID, Entity] = field(
        default_factory=dict, metadata="Игровые обьекты"
    )
    systems: Dict[Type[System], System] = field(
        default_factory=dict, metadata="Системы игрового мира"
    )
    resources: Dict[str, Any] = field(
        default_factory=dict, metadata="Ресурсы"
    )
    status: GameStatus = field(
        default=GameStatus.start, metadata="Состояние сцены"
    )

    def get_resource(self, key: str) -> Optional[Any]:
        return self.resources.get(key)

    def add_resource(self, key: str, value: Any) -> bool:
        if key in self.resources:
            return False
        self.resources[key] = value
        return True

    def delete_resource(self, key: str) -> bool:
        if key in self.resources:
            del self.resources[key]
            return True
        return False

    def get_system(self, system: Type[System]) -> Optional[System]:
        return self.systems.get(system)

    def add_system(self, system: System) -> bool:
        if type(system) in self.systems:
            return False
        self.systems[type(system)] = system
        return True

    def delete_system(self, system: Type[System]) -> bool:
        if system in self.systems:
            del self.systems[system]
            return True
        return False

    def get_entity(self, entity_id: UUID) -> Optional[Entity]:
        return self.entities.get(entity_id)

    def add_entity(self, entity: Entity) -> bool:
        if type(entity) in self.entities:
            return False
        self.entities[entity.get_uuid()] = entity
        return True

    def delete_entity(self, entity_id: UUID) -> bool:
        if entity_id in self.entities:
            del self.entities[entity_id]
            return True
        return False

    def get_component(self, entity_id: UUID, component: Type[Component]) -> Optional[Component]:
        entity: Optional[Entity] = self.get_entity(entity_id=entity_id)
        if entity is not None:
            return entity.get_component(component)

    def add_component(self, entity_id: UUID, component: Component) -> bool:
        if entity := self.get_entity(entity_id):
            return entity.add_component(component)
        return False

    def delete_component(self, entity_id: UUID, component: Type[Component]) -> bool:
        if entity := self.get_entity(entity_id):
            return entity.delete_component(component)
        return False

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

    def set_status(self, status: GameStatus) -> None:
        self.status = status

    def init(self) -> None:
        world: Entity = new_world(5, 5)
        self.add_entity(world)
        self.status = GameStatus.dialog

    def dialog(self) -> None:
        from src.systems.ui.dialog import SystemDialog
        dialog: Optional[UUID] = self.get_resource("dialog")
        if dialog is None:
            raise RuntimeError("Не найден Entity для генерация экрана")
        if system := self.get_system(SystemDialog):
            system: SystemDialog
            system.dialog(scene=self, entity_id=dialog)
        else:
            raise RuntimeError("Не найдена система для генерация экрана")

    def new_world(self) -> None:
        from src.systems.ui.dialog import SystemDialog
        from src.systems.ui.system_exit import SystemExit
        from src.systems.ui.system_input import SystemInput
        from src.systems.ui.display import SystemDisplay

        base_dialog: Entity = new_base_dialog()
        self.add_entity(base_dialog)
        self.add_resource("dialog", base_dialog.get_uuid())
        self.add_system(SystemExit())
        self.add_system(SystemInput())
        self.add_system(SystemDialog())
        self.add_system(SystemDisplay())

    def run(self) -> None:

        while True:
            if self.status == GameStatus.start:
                self.init()
            elif self.status == GameStatus.dialog:
                self.dialog()
            elif self.status == GameStatus.runner:
                for system in self.systems.values():
                    system.process(scene=self)
            elif self.status == GameStatus.exit:
                exit()
