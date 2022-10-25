from dataclasses import dataclass

@dataclass
class Tile:
    x : int
    y : int
    piece : object = None