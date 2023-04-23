from typing import Union


class Tile:
    small = None
    big = None

    def __init__(self, face_one: int = None, face_two: int = None, existing_tile: 'Tile' = None) -> 'Tile':
        if (not face_one) or (not face_two) or (not existing_tile):
            return None
        if existing_tile:
            self.small = existing_tile.small
            self.big = existing_tile.big
        else:
            self.small = min(face_one, face_two)
            self.big = max(face_one, face_two)
        return self

    def valid(self, other_tile: 'Tile') -> bool:
        other_tile = Tile(other_tile)
        if self.small and self.big:
            return self.small == other_tile.small or \
                self.small == other_tile.big or \
                self.big == other_tile.small or \
                self.big == other_tile.big
        return False

    def __eq__(self, rhs: 'Tile'):
        return self.small == rhs.small and self.big == rhs.big

    def __str__(self) -> str:
        return "[" + str(self.small) + "/" + str(self.big) + ']'

    def __call__(self, rhs: 'Tile') -> bool:
        return rhs.small != None and rhs.big != None

    def __hash__(self):
        return hash(str(self))

    def null_tile(self) -> bool:
        if self.small and self.big:
            return False
        return True
