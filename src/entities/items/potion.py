from typing import List

from src.core.scene import Scene
from src.entities.base import Entity
from src.systems.items.potion import SystemPotion
from src.components.unit.item import ComponentItem
from src.components.items.potion import ComponentPotion
from src.components.ui.dialog import (
    ComponentDialog,
    ComponentDialogRender
)


def create_item_potion(scene: Scene, hp: int = 100) -> Entity:
    entity: Entity = Entity()
    renderings: List[ComponentDialogRender] = [
        ComponentDialogRender(
            system_type=SystemPotion,
            entity_id=entity.get_uuid(),
            component=ComponentDialog,
            next_dialog=entity.get_uuid()
        )
    ]
    entity.add_component(ComponentItem(
        name=f"Зелье воставноления жизней {hp}",
        system_type=SystemPotion
    ))
    entity.add_component(ComponentDialog(renderings=renderings))
    entity.add_component(ComponentPotion(hp=hp))
    scene.add_entity(entity=entity)
    return entity
