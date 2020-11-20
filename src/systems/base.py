from typing import TYPE_CHECKING
from abc import ABC, abstractmethod

if TYPE_CHECKING:
    from src.core.scene import Scene


class System(ABC):

    @abstractmethod
    def process(self, scene: "Scene"):
        pass

    def event(self, scene: "Scene"):
        pass
