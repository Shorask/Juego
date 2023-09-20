from typing import DefaultDict
'''
import pygame, sys

#Inicio
pygame. init()
ventana= pygame.display#.set_mode((500,400))
ventana.init()
#pygame.display.set_caption('RACEBOAT')
ventana.set_mode((500,400))
ventana.set_caption('RACEBOAT')

#Bucle para que no se cierre la ventana del juego
while True:
  for event in pygame.event.get():
    if event.type == quit:
        pygame.quit()
        sys.exit()
    #pygame.display.update()
    ventana.update()
#Fin del bucle
DefaultDict

#Paleta de colores
azul_mar= (60, 161, 196)
verde_amazonas= (44, 180, 61)
azul_rio= (71, 137, 115)
gris_obstaculos= (85, 122, 88)
arena_nilo=(224, 180, 28)
blanco=(255,255,255)
#Fin paleta de colores

#Figuras geometricas
ventana.pygame.draw.rect()
ventana.fill(blanco)
pygame.display.flip()'''

import pygame

azul_mar= (60, 161, 196)
verde_amazonas= (44, 180, 61)
azul_rio= (71, 137, 115)
gris_obstaculos= (85, 122, 88)
arena_nilo=(224, 180, 28)
blanco=(255,255,255)
pygame.init()
ventana=pygame.display.set_mode((500,400))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            False
    ventana.fill((azul_rio))
    pygame.display.flip()
    pygame.time.Clock().tick(60)
pygame.quit()


