from tile import Tile
from player import Player
from typing import MutableSet
from typing import Union


class NPCPlayer(Player):

    def __init__(self) -> None:
        pass

    def play(self, played: Tile) -> Union[bool, Tile]:
        if not isinstance(played, Tile):
            # can't play something that isn't a tile
            return False
        if played.null_tile():
            # can't play a null tile
            return False

        # Don't know the NPC's hand so we just add it before playing it
        super().add_hand(played)
        return super().play(played)
