from uuid import uuid4, UUID
from typing import Type, Dict, Optional
from dataclasses import dataclass, field

from src.components.base import Component


@dataclass
class Entity:
    entity_id: UUID = field(default_factory=uuid4, metadata="Id Обьекта")
    components: Dict[Type[Component], Component] = field(
        default_factory=list, metadata="Компоненты обьекта"
    )

    def get_component(self, component: Type[Component]) -> Optional[Component]:
        return self.components.get(component)
