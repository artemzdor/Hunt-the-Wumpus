from uuid import UUID
from typing import List

from src.core.scene import Scene
from src.entities.base import Entity
from src.systems.unit.item import SystemItem
from src.components.unit.inventory import ComponentInventory
from src.components.ui.dialog import (
    ComponentDialogRender,
    ComponentDialog
)


def new_entity_item(scene: Scene, player: Entity) -> UUID:
    entity: Entity = Entity(
        tags=["Items"]
    )
    renderings: List[ComponentDialogRender] = [
        ComponentDialogRender(
            system_type=SystemItem,
            entity_id=player.get_uuid(),
            component=ComponentInventory,
            next_dialog=player.get_uuid()
        ),
    ]
    dialog: ComponentDialog = ComponentDialog(
        renderings=renderings
    )
    entity.add_component(dialog)
    scene.add_entity(entity=entity)
    return entity.get_uuid()
