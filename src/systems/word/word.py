from uuid import UUID
from typing import List, Optional, Tuple

from src.core.scene import Scene
from src.systems.base import System
from src.entities.base import Entity
from src.components.world.position import ComponentPosition
from src.components.world.coordinates import ComponentCoordinates


class SystemWord(System):
    word_entity: Entity
    coordinates: ComponentCoordinates

    def __init__(self, word_entity: Entity):
        self.word_entity = word_entity
        if coordinates := self.word_entity.get_component(
                ComponentCoordinates
        ):
            self.coordinates = coordinates
        else:
            raise RuntimeError("Не найден компонент при иницилизации "
                               "SystemWord (ComponentCoordinates)")

    def get_width(self) -> int:
        """Ширина мира (X)"""
        return self.coordinates.width

    def get_height(self) -> int:
        """Высота мира (Y)"""
        return self.coordinates.height

    def get_word(self) -> List[List[List[Entity]]]:
        """Кординатная сетка местности"""
        return self.coordinates.word

    def is_boundary(self, x: int, y: int) -> bool:
        """Проверка на границы мира"""
        if 0 <= x <= self.get_width():
            if 0 <= y <= self.get_height():
                return True

    def is_filter(self, x: int, y: int) -> bool:
        """Общий фитр проверок доступности кординат"""
        return self.is_boundary(x=x, y=y)

    def get_point(self, x: int, y: int) -> Optional[List[Entity]]:
        """Получение всех обьектов в точке x, y"""
        if self.is_filter(x=x, y=y):
            return self.get_word()[x][y]

    def is_move(self, x: int, y: int) -> bool:
        """Проверка можно ли обьекту перемещатся в точку x, y"""
        if self.is_filter(x=x, y=y):
            return True
        return False

    def get_entity_point(self, entity_id: UUID,
                         x: int, y: int) -> Optional[Tuple[Entity, int]]:
        """Получение обоектов по кординате x, y"""
        entities: Optional[List[Entity]] = self.get_point(x=x, y=y)

        if entities is None:
            return

        for index, entity in enumerate(entities):
            if entity.get_uuid() == entity_id:
                return entity, index

    def delete_entity_point(self, x: int, y: int, index: int) -> bool:
        """Удаление обоекта по кординате x, y"""
        if point := self.get_point(x=x, y=y):
            del point[index]
            return True
        return False

    def add_entity_point(self, x: int, y: int, entity: Entity) -> bool:
        """Добавление обоекта по кординате x, y"""
        if point := self.get_point(x=x, y=y):
            point.append(entity)
            return True
        return False

    def set_move(self, entity_id: UUID, component: ComponentPosition, move_x: int, move_y: int) -> bool:
        """Перемещение обьекта"""
        x: int = component.x
        y: int = component.y

        entity: Optional[Tuple[Entity, int]] = self.get_entity_point(
            entity_id=entity_id, x=x, y=y
        )

        if entity is None or not self.is_move(x=x, y=y) or not self.is_move(x=move_x, y=move_y):
            return False

        delete: bool = self.delete_entity_point(x=x, y=y, index=entity[1])

        if not delete:
            raise RuntimeError("Не удалось удалить обьект в point")

        add_point: bool = self.add_entity_point(x=move_x, y=move_y, entity=entity[0])
        component.x = move_x
        component.y = move_y

        # TODO: Передача события системе перемещиния
        return add_point

    def process(self, scene: Scene):
        pass

