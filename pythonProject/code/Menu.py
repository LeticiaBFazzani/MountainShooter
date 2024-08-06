#!/usr/bin/python
#-*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, C_ORANGE, C_WHITE, MENU_OPTION, C_YELLOW


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png')  # carregar imagem
        self.rect = self.surf.get_rect(left=0, top=0)  # inserir imagem em forma de tela com as posições

    def run(self):
        menu_option = 0
        pygame.mixer_music.load('./asset/Menu.mp3')  # carregar musica
        pygame.mixer_music.play(-1)  # tocar a musica

        while True:  # loop infinito para apresentar a imagem (desenhando imagens)
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Moutain", C_ORANGE, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "Shooter", C_ORANGE, ((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], C_YELLOW, ((WIN_WIDTH / 2), 200 + 25 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i))

            pygame.display.flip()

            # check for all events (analise para todos eventos)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # adicionando o evento para tirar erro de fechar a janela
                    pygame.quit()  # fechar janela
                    quit()  # encerrar jogo
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  # Descer as opções (tecla p/ baixo)
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:  # subir as opções (tecla p/ cima)
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:  # ENTER
                        return MENU_OPTION[menu_option]



    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter",size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

