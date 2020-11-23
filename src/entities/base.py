from uuid import uuid4, UUID
from dataclasses import dataclass, field
from typing import Type, Dict, Optional, List

from src.components.base import Component


@dataclass
class Entity:
    entity_id: UUID = field(default_factory=uuid4, metadata="Id Обьекта")
    components: Dict[Type[Component], Component] = field(
        default_factory=dict, metadata="Компоненты обьекта"
    )
    tags: List[str] = field(default_factory=list, metadata="Теги")

    def get_component(self, component: Type[Component]) -> Optional[Component]:
        return self.components.get(component)

    def get_uuid(self) -> UUID:
        return self.entity_id

    def add_component(self, component: Component) -> bool:
        if type(component) in self.components:
            return False
        self.components[type(component)] = component
        return True

    def delete_component(self, component: Type[Component]) -> bool:
        if component in self.components:
            del self.components[component]
            return True
        return False
