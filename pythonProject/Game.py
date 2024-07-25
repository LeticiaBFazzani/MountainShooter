#!/usr/bin/python
#-*- coding: utf-8 -*-
import pygame

from Menu import Menu


class Game:
    def __init__(self):

        pygame.init()
        self.window = pygame.display.set_mode(size=(600, 480))  # criando a janela que rodará o jogo

    def run(self):

        while True:
            menu = Menu(self.window)
            menu.run()
            pass

            # check for all events (analise para todos eventos)
         #   for event in pygame.event.get():
            #    if event.type == pygame.QUIT:  # adicionando o evento para tirar erro de fechar a janela

              #      pygame.quit()  # comando para fechar janela
               #     quit()  # encerra o pygame

