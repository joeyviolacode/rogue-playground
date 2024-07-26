from __future__ import annotations

from typing import TYPE_CHECKING

from tcod.context import Context
from tcod.console import Console

from actions import Action, MovementAction, EscapeAction
from game_map import GameMap
from input_handlers import EventHandler
from tcod.map import compute_fov

if TYPE_CHECKING:
    from entity import Entity
    from game_map import GameMap

class Engine:
    game_map: GameMap

    def __init__(self, player: Entity):
        self.event_handler : EventHandler = EventHandler(self)
        self.player = player

    def handle_enemy_turns(self) -> None:
        for entity in set(self.game_map.entities) - {self.player}:
            if self.game_map.visible[entity.x, entity.y]:
                print(f"The {entity.name} stands around, twiddling its thumbs.")

    def update_fov(self) -> None:
        self.game_map.visible[:] = compute_fov(
            self.game_map.tiles["transparent"],
            (self.player.x, self.player.y),
            radius=8,
        )
        self.game_map.explored |= self.game_map.visible

    def render(self, console: Console, context: Context) -> None:
        self.game_map.render(console)

        context.present(console)

        console.clear()