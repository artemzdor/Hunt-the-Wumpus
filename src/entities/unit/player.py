from uuid import UUID
from typing import List

from src.core.scene import Scene
from src.entities.base import Entity
from src.components.base import Component
from src.components.world.position import ComponentPosition
from src.components.unit.healthy import ComponentUnitHealthy
from src.components.unit.inventory import ComponentInventory
from src.components.ui.dialog import (
    ComponentDialogRender,
    ComponentDialog
)

from src.entities.items.potion import create_item_potion
from src.entities.unit.items import new_entity_items


def create_player_dialogs(entity: Entity) -> List[ComponentDialogRender]:
    from src.systems.ui.info import SystemInfo
    from src.systems.word.move import SystemMove
    from src.systems.ui.system_exit import SystemExit
    from src.systems.unit.inventory import SystemInventory

    renderings: List[ComponentDialogRender] = [
        ComponentDialogRender(
            system_type=SystemInfo,
            entity_id=entity.get_uuid(),
            component=Component,
            next_dialog=entity.get_uuid()
        ),
        ComponentDialogRender(
            system_type=SystemExit,
            entity_id=entity.get_uuid(),
            component=Component,
            next_dialog=entity.get_uuid()
        ),
        ComponentDialogRender(
            system_type=SystemMove,
            entity_id=entity.get_uuid(),
            component=ComponentPosition,
            next_dialog=entity.get_uuid()
        ),
        ComponentDialogRender(
            system_type=SystemInventory,
            entity_id=entity.get_uuid(),
            component=ComponentInventory,
            next_dialog=entity.get_uuid()
        ),
    ]
    return renderings


def create_player_entity(scene: Scene) -> Entity:
    entity: Entity = Entity(tags=["player"])

    renderings: List[ComponentDialogRender] = create_player_dialogs(
        entity=entity
    )

    dialog: ComponentDialog = ComponentDialog(
        renderings=renderings
    )

    entity_items: UUID = new_entity_items(scene=scene, player=entity)
    entity_potion: Entity = create_item_potion(scene=scene)
    items: List[UUID] = [entity_potion.get_uuid()]

    components: List[Component] = [
        ComponentUnitHealthy(healthy=50, healthy_max=100, revival=0),
        ComponentPosition(x=0, y=0, speed=1),
        ComponentInventory(
            items=items,
            entity_items=entity_items,
            next_dialog=entity.get_uuid()),
        dialog
    ]

    for component in components:
        entity.add_component(component)

    return entity
