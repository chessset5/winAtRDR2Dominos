from typing import Union


class Tile:
    small = None
    big = None

    def __init__(self, face_one: int = None, face_two: int = None, existing_tile: 'Tile' = None) -> None:
        '''
        Accpets int and int or an existing Tile.
        ints are pip halfs of the domino.
        🁢	🁣	🁤	🁥	🁦	🁧	🁨	🁩	🁪	🁫	🁬	🁭	🁮	🁯
        🁰	🁱	🁲	🁳	🁴	🁵	🁶	🁷	🁸	🁹	🁺	🁻	🁼	🁽	🁾	🁿
        🂀	🂁	🂂	🂃	🂄	🂅	🂆	🂇	🂈	🂉	🂊	🂋	🂌	🂍	🂎	🂏
        🂐	🂑	🂒	🂓
        ints are accepted 0-6.
        If one of the ints is out of range the pips will be null
        '''
        if isinstance(face_one, int) and isinstance(face_two, int):
            self.small = min(face_one, face_two)
            self.big = max(face_one, face_two)
            if self.small < 0 or self.small > 6 or self.big < 0 or self.big > 6:
                self.small = None
                self.big = None
                return None
        elif isinstance(existing_tile, Tile):
            self.small = existing_tile.small
            self.big = existing_tile.big
        else:
            return None

    def valid(self, other: 'Tile') -> bool:
        '''
        Validate if the given tile is compatable with current tile.
        IE 0/0 0/1, 0/1 2/0, etc etc;
        True if one of the pips on either half of the tile is the same as one of the pips on the other tile. False otherwise.
        '''
        if not isinstance(other, Tile):
            return NotImplemented
        if self.small and self.big:
            return self.small == other.small or \
                self.small == other.big or \
                self.big == other.small or \
                self.big == other.big
        return False


    # region class defaults


    def __str__(self) -> str:
        return f"[{self.small}/{self.big}]"

    def __repr__(self) -> str:
        return str(self)

    def __call__(self, rhs: 'Tile') -> bool:
        return rhs.small != None and rhs.big != None

    def __hash__(self):
        return hash(str(self))

    def __eq__(self, other: 'Tile'):
        return self.small == other.small and self.big == other.big

    def __lt__(self, other: 'Tile') -> bool:
        if isinstance(other, Tile):
            if self.small == other.small:
                return self.big < other.big
            return self.small < other.small
        else:
            return NotImplemented

    def __gt__(self, other: 'Tile') -> bool:
        if isinstance(other, Tile):
            return (not self < other) and (self != other)
        else:
            return NotImplemented
        
    # endregion

    def null_tile(self) -> bool:
        '''
        returns true if both pips are None
        '''
        if self.small and self.big:
            return False
        return True
