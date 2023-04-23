from tile import Tile
from player import Player
from typing import MutableSet
from typing import Union


def setup(player: int) -> None:
    table: MutableSet[Tile] = MutableSet[Tile]
    mystery_tiles: MutableSet[Tile] = set([
        Tile(i, j) for i in range(7) for j in range(i, 7)])
    pass


def main() -> None:
    players = int(input("how many players:"))
    setup(players)


if __name__ == "__main__":
    main()
