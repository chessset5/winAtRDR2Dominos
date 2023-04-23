from tile import Tile
from typing import MutableSet
from typing import Union


class Player:
    ghost_hand: int = None
    hand: MutableSet[Tile] = None
    played: MutableSet[Tile] = None

    def __init__(self) -> None:
        pass

    def add_hand(self, tile_card: Tile) -> MutableSet[Tile]:
        if not isinstance(tile_card, Tile):
            return None
        self.hand.add(tile_card)
        return self.hand

    def play(self, played: Tile) -> Union[bool, Tile]:
        if not isinstance(played, Tile):
            return False
        if played.null_tile():
            return False

        if played in self.hand:
            self.played.add(played)
            self.hand.remove(played)
            return played
        return False
