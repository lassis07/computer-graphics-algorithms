import pygame
from pygame import gfxdraw

def setPixel(img, x , y, color):
    if x < 0:
        x = 0

    if y < 0:
        y = 0   
 
    gfxdraw.pixel(img, y, x, color)

def main():
    pygame.init()
    pygame.display.set_caption('Set Pixel')
    screen = pygame.display.set_mode((700,700))
    print(screen)
    WHITE = (255,255,255)
    setPixel(screen, 50, 50, WHITE)

    # main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.update()
     
if __name__=="__main__":
    main()