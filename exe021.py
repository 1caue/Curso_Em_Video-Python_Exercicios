import pygame
pygame.init()
# Entre as "()" do pygame.mixer.music você irá colocar o arquivo da musica ou do som
pygame.mixer.music.load()
pygame.mixer.music.play()
pygame.event.wait