from uuid import UUID
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any, Dict

from src.components.base import Component


if TYPE_CHECKING:
    from src.core.scene import Scene


class System(ABC):

    @abstractmethod
    def process(self, scene: "Scene"):
        pass

    def event(self, scene: "Scene", system_event: "System", event_type: str, entity_id: UUID,
              component: Component, value: Any,  value_name: str, kwargs: Dict[str, Any]) -> None:
        pass
