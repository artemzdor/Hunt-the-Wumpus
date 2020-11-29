from uuid import UUID
from typing import Dict, Any, List, Optional

from src.core.scene import Scene
from src.systems.base import System
from src.entities.base import Entity
from src.components.base import Component
from src.systems.ui.dialog import SystemDialog
from src.systems.ui.render import SystemRender
from src.components.unit.item import ComponentItem
from src.components.unit.inventory import ComponentInventory
from src.components.ui.dialog import (
    ComponentDialogEvent,
    ComponentDialog
)


class SystemItem(SystemRender):

    def process(self, scene: Scene):
        pass

    def event(self, scene: Scene, system_event: System, event_type: str, entity_id: UUID,
              component: Component, value: Any, value_name: str, kwargs: Dict[str, Any]) -> None:
        pass

    def render(self, scene: Scene, render_entity_id: UUID, next_dialog: UUID) -> List[ComponentDialogEvent]:
        inventory: Optional[ComponentInventory] = scene.get_component(
            entity_id=render_entity_id, component=ComponentInventory
        )

        if inventory is None:
            raise RuntimeError("Не найден компонен для рендеринга инвентаря")

        renders: List[ComponentDialogEvent] = list()

        q_event: ComponentDialogEvent = ComponentDialogEvent(
            command=f"q",
            display_info="Вернутся в меню",
            system_type=SystemDialog,
            value=None,
            value_name="",
            entity_id=render_entity_id,
            component_type=ComponentDialog,
            next_dialog=render_entity_id,
            info=False
        )

        if len(inventory.items) == 0:
            info_event: ComponentDialogEvent = ComponentDialogEvent(
                command=f"",
                display_info="В инвентаре нет предметов",
                system_type=type(None),
                value=None,
                value_name="",
                entity_id=render_entity_id,
                component_type=Component,
                next_dialog=render_entity_id,
                info=True
            )

            return [info_event, q_event]

        for index, item_uuid in enumerate(inventory.items):
            entity: Optional[Entity] = scene.get_entity(entity_id=item_uuid)

            if entity is None:
                continue

            component_item: Optional[ComponentItem] = entity.get_component(ComponentItem)

            if component_item is None:
                continue

            event: ComponentDialogEvent = ComponentDialogEvent(
                command=f"{index}",
                display_info=component_item.name,
                system_type=component_item.system_type,
                value=None,
                value_name="",
                entity_id=entity.get_uuid(),
                component_type=ComponentItem,
                next_dialog=next_dialog,
            )
            renders.append(event)
        renders.append(q_event)
        scene.set_resource("dialog", render_entity_id)
        return renders
