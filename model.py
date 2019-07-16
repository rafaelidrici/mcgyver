#! /usr/bin/env python3
# coding: utf-8
#
import pygame
import os

class Position:

    def __init__(self, x, y):
        self.position = (x, y)
    
    def __repr__(self):
        return str(self.position)

    def up(self):
        x, y = self.position
        return Position(x-1, y)

    def down(self):
        x, y = self.position
        return Position(x+1, y)

    def right(self):
        x, y = self.position
        return Position(x, y+1)
    
    def left(self):
        x, y = self.position
        return Position(x, y-1)

class Player:
    #
    current_items = []
    
    def __init__(self, x, y, Position):
        self.position = (1, 1)

class Guardian:
    pass
    
class Item:

    list_items = []

    def __init__(self, x, y, Position):
    pass

class Zone:
    pass


    
