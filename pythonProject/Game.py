#!/usr/bin/python
#-*- coding: utf-8 -*-
import pygame

from Menu import Menu
from code.Const import WIN_WIDTH, WIN_HEIGTH


class Game:
    def __init__(self):

        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGTH))  # criando a janela que rodará o jogo

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass



