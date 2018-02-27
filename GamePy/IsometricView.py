# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 11:53:19 2017

Clases para la elaboracion de un mapa en vista
isométrica

@author: Ismael Marin Molina
@date 10/11/2017
"""
import pygame
import random
import sys
import config

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file).convert()
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = location


def PlaceTile(gameDisplay,Terrain, x, y):

    gameDisplay.blit(Terrain,(x,y))
    #pygame.draw.rect(gameDisplay, Ttype, [x,y,config.tileWidth,config.tileHeight])
    """

    This function must do a tranformation 2d to isometric view
    screen.x = (map.x - map.y) * TILE_WIDTH_HALF
    screen.y = (map.x + map.y) * TILE_HEIGHT_HALF
    Also this should draw rombus not square.
    use for this the function pygame.draw.polygon(screen, color ,[vertex],width)

    """

def MapBuilder(gameDisplay):
    random.seed()

    currentRow = 0
    currentTile = 0

    for row in config.map_data:
        Terrain = config.red

        for tilde in row:
            cartx = currentTile * config.tileWidth / 2
            carty = currentRow  * config.tileHeight / 2
            x = 550 + ((cartx - carty) )
            y = 100 + ((cartx + carty) / 2 )
            tileType = tilde

            print ( ((2*x + y) / 2) - 550)

            if tileType == 1:

                Terrain =  pygame.image.load('./PNG/Isometric-Blocks_03.png').convert()
                Terrain.set_colorkey((0,0,0))
            if tileType == 0:
                Terrain =  pygame.image.load('./PNG/Isometric-Blocks_24.png').convert()
                Terrain.set_colorkey((0,0,0))
                PlaceTile (gameDisplay, Terrain, x, y)

                y = y - config.tileHeight/2
                Terrain =  pygame.image.load('./PNG/Isometric-Blocks_03.png').convert()
                Terrain.set_colorkey((0,0,0))
            if tileType == 2:
                y = y + 5
                Terrain =  pygame.image.load('./PNG/isometric-PACK-2_07.png').convert()
                Terrain.set_colorkey((0,0,0))

            PlaceTile (gameDisplay, Terrain, x, y)
            currentTile += 1

        currentTile = 0
        currentRow += 1

def click(posX, posY):

    pass

def main():
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode(config.SIZE, pygame.DOUBLEBUF)
    pygame.display.set_caption('3D')
    clock = pygame.time.Clock()

    BackGround = Background('sky2.jpg',[0,0])
    DISPLAYSURF.fill([255,255,255])
    DISPLAYSURF.blit(BackGround.image, BackGround.rect)

    Tree =  pygame.image.load('./Medieval/oaktree.png').convert()
    Tree.set_colorkey((0,0,0))
    cartx = 0  * config.tileWidth / 2
    carty = (len(config.map_data) - 3)  * config.tileHeight / 2
    tx = 460 + ((cartx - carty) )
    ty = 100 + ((cartx + carty) / 2 )

    cartx = 3  * config.tileWidth / 2
    carty = 1  * config.tileHeight / 2
    cx = 550 + ((cartx - carty) )
    cy = 100 + ((cartx + carty) / 2 )

    print(config.map_data[1][3])

    print(cx , cy)

    House =  pygame.image.load('./Medieval/house.png').convert()
    #House.set_colorkey((0,0,0))
    cartx = 3  * config.tileWidth / 2
    carty = 5  * config.tileHeight / 2
    hx = 360 + ((cartx - carty) )
    hy = 100 + ((cartx + carty) / 2 )

    MapBuilder(DISPLAYSURF)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        pygame.draw.circle(DISPLAYSURF, config.black, [cx.__int__(), cy.__int__()], 2)
        pygame.display.flip()
        DISPLAYSURF.fill([255,255,255])
        DISPLAYSURF.blit(BackGround.image, BackGround.rect)
        MapBuilder(DISPLAYSURF)
        #DISPLAYSURF.blit(Tree,(tx,ty))
        #DISPLAYSURF.blit(House,(hx,hy))
        pygame.draw.circle(DISPLAYSURF, config.black, [cx.__int__(), cy.__int__()], 2)
        clock.tick(config.FPS)




if __name__ == "__main__":
    main()
