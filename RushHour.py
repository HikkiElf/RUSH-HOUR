import tkinter as tk
from PIL import ImageTk, Image
import random

# class for tiles info
class Tile:

    def __init__(self, size, direction, tileCoordX, tileCoordY, keyTile):

        self.size = size # 2, 3

        self.direction = direction # horizontal, vertical

        self.tileCoordX = tileCoordX # X tile coordinate
        self.tileCoordY = tileCoordY # Y tile coordinate

        self.tileIndexX = None # X index to choose tile
        self.tileIndexY = None # Y index to choose tile

        self.tileStatus = "UNSELECT"

        self.keyTile = keyTile
    
    def set_coords(self, tileCoordX, tileCoordY):
        self.tileCoordX = tileCoordX
        self.tileCoordY = tileCoordY
    
    def get_index(self):
        self.tileIndexX = self.tileCoordX // squareSize
        self.tileIndexY = self.tileCoordY // squareSize
    
    def set_direction(self, direction):
        self.direction = direction
    
    def set_size(self, size):
        self.size = size

    def set_status(self, TileStatus):
        self.tileStatus = tileStatus

    def description(self):
        print("size =", self.size, " direction =", self.direction, " TileCoordX =", 
            self.TileCoordX, " TileCoordY =", self.TileCoordY, " TileStatus =", self.TileStatus)

class Field:

    def __init__(self, boardSize):
        self.boardSize = boardSize
        self.emptySq
