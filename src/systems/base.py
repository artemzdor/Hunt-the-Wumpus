from abc import ABC, abstractmethod

from src.core.scene import Scene


class System(ABC):

    @abstractmethod
    def process(self, scene: Scene):
        pass
