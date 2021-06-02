import tkinter as tk
from PIL import ImageTk, Image
import random

# class for tiles info
class tile:

    def __init__(self):

        self.size = None # 2, 3

        self.direction = None # horizontal, vertical

        self.tileCoordX = None # X tile coordinate
        self.tileCoordY = None # Y tile coordinate

        self.tileIndexX = None # X index to choose tile
        self.TileIndexY = None # Y index to choose tile

        self.tileStatus = "UNSELECT"
    
    def set_coords(self, tileCoordX, tileCoordY):
        self.tileCoordX = TileCoordX
        self.tileCoordY = TileCoordY
    
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

class field:

    def __ini

