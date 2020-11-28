from typing import List

from src.entities.base import Entity
from src.components.base import Component
from src.components.unit.healthy import ComponentUnitHealthy
from src.components.world.position import ComponentPosition
from src.components.ui.dialog import (
    ComponentDialogRender,
    ComponentDialog
)


def create_player_dialogs(entity: Entity) -> List[ComponentDialogRender]:
    from src.systems.ui.system_exit import SystemExit
    from src.systems.word.move import SystemMove
    from src.systems.ui.info import SystemInfo

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
        )
    ]
    return renderings


def create_player_entity() -> Entity:
    entity: Entity = Entity(tags=["player"])

    renderings: List[ComponentDialogRender] = create_player_dialogs(
        entity=entity
    )

    dialog: ComponentDialog = ComponentDialog(
        renderings=renderings
    )
    components: List[Component] = [
        ComponentUnitHealthy(healthy=100, healthy_max=100, revival=0),
        ComponentPosition(x=0, y=0, speed=1),
        dialog
    ]

    for component in components:
        entity.add_component(component)

    return entity
