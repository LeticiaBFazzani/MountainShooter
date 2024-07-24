import pygame

print('Setup start')
pygame.init()
window = pygame.display.set_mode(size=(600, 480)) # criando a janela que rodará o jogo
print('Setup End')

print('loop start')
while True:
    # check for all events (analise para todos eventos)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #adicionando o evento para tirar erro de fechar a janela
            print('Quitting...')
            pygame.quit() # comando para fechar janela
            quit() # encerra o pygame
