from typing import Dict, Type

from src.entities.base import Entity
from src.components.base import Component
from src.components.ui.welcome import ComponentWelcome


def new_welcome() -> Entity:
    components: Dict[Type[Component], Component] = {
        ComponentWelcome: ComponentWelcome()
    }
    entity: Entity = Entity(
        components=components
    )
    return entity
