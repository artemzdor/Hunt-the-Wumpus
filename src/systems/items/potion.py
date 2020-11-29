from uuid import UUID
from typing import Dict, Any, List, Optional

from src.core.scene import Scene
from src.systems.base import System
from src.entities.base import Entity
from src.components.base import Component
from src.systems.ui.render import SystemRender
from src.systems.unit.healthy import SystemUnitHealthy
from src.components.items.potion import ComponentPotion
from src.components.ui.dialog import ComponentDialogEvent
from src.components.unit.inventory import ComponentInventory


class SystemPotionY(SystemRender):

    def process(self, scene: Scene):
        pass

    def enable_potion(
            self, scene: Scene,
            item_entity_id: UUID,
            component_inventory: ComponentInventory,
            component_potion: ComponentPotion,
            player: Entity
    ) -> None:
        if system := scene.get_system(SystemUnitHealthy):
            system: SystemUnitHealthy
            system.add_healthy(healthy=component_potion.hp, entity_id=player.get_uuid(), scene=scene)

        for index, item in enumerate(component_inventory.items.copy()):
            if item == item_entity_id:
                component_inventory.items.pop(index)
                break

        scene.delete_entity(entity_id=item_entity_id)

    def event(self, scene: Scene, system_event: System, event_type: str, entity_id: UUID,
              component: Component, value: Any, value_name: str, kwargs: Dict[str, Any]) -> None:

        player_uuid: UUID = scene.get_resource("player")
        player: Entity = scene.get_entity(entity_id=player_uuid)
        component_inventory: Optional[ComponentInventory] = player.get_component(
            ComponentInventory
        )

        if component_inventory is None:
            raise RuntimeError("Не найден компонент инветаря при использование зелья")

        if isinstance(value, bool) and value:
            self.enable_potion(
                scene=scene,
                item_entity_id=entity_id,
                component_inventory=component_inventory,
                component_potion=component,
                player=player
            )

        scene.set_resource("dialog", component_inventory.entity_items)


class SystemPotion(SystemRender):

    def process(self, scene: Scene):
        pass

    def event(self, scene: Scene, system_event: System, event_type: str, entity_id: UUID,
              component: Component, value: Any, value_name: str, kwargs: Dict[str, Any]) -> None:
        if value is None:
            scene.set_resource("dialog", entity_id)

    def render(self, scene: Scene, render_entity_id: UUID, next_dialog: UUID) -> List[ComponentDialogEvent]:
        event_v: ComponentDialogEvent = ComponentDialogEvent(
            command="v",
            display_info="Выпить",
            system_type=SystemPotionY,
            kwargs={},
            value=True,
            value_name="",
            entity_id=render_entity_id,
            component_type=ComponentPotion,
            next_dialog=next_dialog,
        )
        event_q: ComponentDialogEvent = ComponentDialogEvent(
            command="q",
            display_info="Вернутся в инвентарь",
            system_type=SystemPotionY,
            kwargs={},
            value=False,
            value_name="",
            entity_id=render_entity_id,
            component_type=ComponentPotion,
            next_dialog=next_dialog,
        )
        scene.set_resource("dialog", render_entity_id)
        return [event_v, event_q]
