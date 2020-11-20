from enum import IntEnum


class GameStatus(IntEnum):
    start = 1
    dialog = 2
    runner = 3
    stop = 4
    exit = 5
