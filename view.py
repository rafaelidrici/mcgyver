#! /usr/bin/env python3
# coding: utf-8
#
import pygame 
import time
import os
from random import*

class MenuView:
    white = (255,255,255)

    pygame.init()

    surfaceW = 1000
    surfaceH = 600

    surface = pygame.display.set_mode((surfaceW,surfaceH))
    pygame.display.set_caption("Aidez McGyver à s'échapper !")
    clock = pygame.time.Clock()

    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over= True

pass

class PlayerView:

    #
    #   Player graphical representation
    #
    
    pass

class GuardianView:
    pass
    
class ZoneView:
    pass  

class ItemView:
    pass