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

class Tile(pygame.sprite.Sprite):
    def __init__(self, image_type, location):
        self.image_type = image_type
        self.location = location
        pass

    def PlaceTile(self, gameDisplay):
        cartx = self.location[0] * config.tileWidth / 2
        carty = self.location[1] * config.tileHeight / 2

        cor_X = [cartx, cartx + config.tileWidth]
        cor_Y = [carty, carty + config.tileHeight]

        point_x = ((self.location[0] + 1) * config.tileWidth / 2 )
        point_y = (self.location[1] * config.tileHeight / 2)

        x = config.offset_x + ((cartx - carty))
        y = config.offset_y + ((cartx + carty) / 2)

        px = config.offset_x + ((point_x - point_y))
        py = config.offset_y + ((point_x + point_y) / 2)


        if self.image_type == 1:
            Terrain =  pygame.image.load('./PNG/Isometric-Blocks_03.png').convert()
            Terrain.set_colorkey((0,0,0))
        if self.image_type == 0:
            Terrain =  pygame.image.load('./PNG/Isometric-Blocks_24.png').convert()
            Terrain.set_colorkey((0,0,0))
            PlaceTile (gameDisplay, Terrain, x, y)
            y = y - config.tileHeight/2
            Terrain =  pygame.image.load('./PNG/Isometric-Blocks_03.png').convert()
            Terrain.set_colorkey((0,0,0))
        if self.image_type == 2:
            y = y + 5
            Terrain =  pygame.image.load('./PNG/isometric-PACK-2_07.png').convert()
            Terrain.set_colorkey((0,0,0))

        rect = Terrain.get_rect()

        print(rect[0], rect.y)

        gameDisplay.blit(Terrain, (x, y))
        pygame.draw.circle(gameDisplay, config.blue, [int(x), int(y)], int(config.tileWidth /16))
        pygame.draw.circle(gameDisplay, config.red, [int(px), int(py)], int(config.tileWidth /8))
        pass

    def __str__(self):
        cartx = self.location[0] * config.tileWidth / 2
        carty = self.location[1] * config.tileHeight / 2
        y = config.offset_y + ((cartx + carty) / 2)
        x = config.offset_x + ((cartx - carty))
        print(str(cartx) + "  " + str(carty))
        print(str(x) + " " + str(y))
        pass




    """

    This function must do a tranformation 2d to isometric view
    screen.x = (map.x - map.y) * TILE_WIDTH_HALF
    screen.y = (map.x + map.y) * TILE_HEIGHT_HALF
    Also this should draw rombus not square.
    use for this the function pygame.draw.polygon(screen, color ,[vertex],width)

    """
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
"""

def main():
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode(config.SIZE, pygame.DOUBLEBUF)
    pygame.display.set_caption('3D')
    clock = pygame.time.Clock()

    BackGround = Background('sky2.jpg',[0,0])
    DISPLAYSURF.fill([255,255,255])
    DISPLAYSURF.blit(BackGround.image, BackGround.rect)

    tile1 = Tile(1,(0,0))
    tile2 = Tile(2,(1,0))
    tile3 = Tile(1,(0,1))
    """
    la y decrece es decir cuanto menos y mas bajo
    la x crece en la direccion sureste
    """
    #MapBuilder(DISPLAYSURF)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        pygame.display.flip()
        DISPLAYSURF.fill([255,255,255])
        DISPLAYSURF.blit(BackGround.image, BackGround.rect)
        tile1.PlaceTile(DISPLAYSURF)
        tile2.PlaceTile(DISPLAYSURF)
        tile3.PlaceTile(DISPLAYSURF)
        #MapBuilder(DISPLAYSURF)
        #DISPLAYSURF.blit(Tree,(tx,ty))
        #DISPLAYSURF.blit(House,(hx,hy))
        clock.tick(config.FPS)




if __name__ == "__main__":
    main()
