from typing import TYPE_CHECKING, Any, Dict
from abc import ABC, abstractmethod

from src.components.base import Component


if TYPE_CHECKING:
    from src.core.scene import Scene


class System(ABC):

    @abstractmethod
    def process(self, scene: "Scene"):
        pass

    def event(self, scene: "Scene", system_event: "System", event_type: str,
              component: Component, value: Any,  value_name: str, kwargs: Dict[str, Any]) -> None:
        pass
