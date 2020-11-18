from pprint import pprint
from typing import Dict, Type, List

from src.entities.base import Entity
from src.components.base import Component
from src.components.world.coordinates import ComponentCoordinates


def _new_word_coordinates(
        width: int, height: int
) -> List[List[List[Entity]]]:
    """Генерим карту мира заполняет Entity пустышками"""
    coordinates: List[List[List[Entity]]] = [
        [[Entity()] for _ in range(width)]
        for _ in range(height)
    ]
    return coordinates


def new_world(width: int, height: int) -> Entity:
    """Создать мир с начальными пустышками картой"""
    word: List[List[List[Entity]]] = _new_word_coordinates(
        width=width, height=height
    )

    components: Dict[Type[Component], Component] = {
        ComponentCoordinates: ComponentCoordinates(
            word=word,
            width=width,
            height=height,
        )
    }
    entity: Entity = Entity(
        components=components
    )
    return entity


if __name__ == '__main__':
    n = new_world(5, 5)
    pprint(n.components[ComponentCoordinates].word[0][0])