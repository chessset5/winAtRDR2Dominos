from tile import Tile
from player import Player
from typing import MutableSet
from typing import Union


def print_Tiles(tiles: MutableSet[Tile]) -> None:
    printlist = list(tiles)
    printlist.sort()
    print(printlist)


def setup(player: int) -> None:
    table: MutableSet[Tile] = set()
    dominos: MutableSet[Tile] = set()
    for i in range(7):
        for j in range(i, 7):
            dominos.add(Tile(face_one=i, face_two=j))
    if Tile() in dominos:
        dominos.remove(Tile())
    print_Tiles(dominos)


def main() -> None:
    players = int(input("how many players:"))
    setup(players)


if __name__ == "__main__":
    main()
