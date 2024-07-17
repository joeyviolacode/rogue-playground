from typing import Tuple

class Entity:
    def __init__(self, x: int, y: int, char: str, color: Tuple):
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    def move(self, dx: int, dy: int):
        self.x += dx
        self.y += dy