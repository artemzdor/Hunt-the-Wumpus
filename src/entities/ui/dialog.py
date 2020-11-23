from typing import List

from src.entities.base import Entity
from src.components.base import Component
from src.components.ui.dialog import (
    ComponentDialog,
    ComponentDialogRender
)


def new_base_dialog() -> Entity:
    from src.systems.ui.system_exit import SystemExit
    entity: Entity = Entity()
    renderings: List[ComponentDialogRender] = [
        ComponentDialogRender(
            system_type=SystemExit,
            entity_id=entity.get_uuid(),
            component=Component,
            next_dialog=entity.get_uuid()
        )
    ]
    dialog: ComponentDialog = ComponentDialog(
        renderings=renderings
    )
    entity.add_component(dialog)

    return entity
