
import pygame, sys
from pygame.locals import *

  

FPS = 60
screen_width = 1890
screen_height = 940
SIZE = (screen_width, screen_width)
BOUND = (0, 0, screen_width, (screen_height-400))
screen = pygame.display.set_mode((screen_width, screen_height))



class man(pygame.sprite.Sprite):
    movespeed = 5

    def __init__(self, initial_pos, bound):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(r'Man.png')
        self.rect = self.image. get_rect()
        self.rect.topleft = initial_pos
        self.bound = bound
        # define the bound limit the man in the upper level
    
    def Moveleft(self):
        if  self.rect.left - self.movespeed >= self.bound[0]:
            self.rect.left -= self.movespeed
        elif self.rect.left - self.movespeed < self.bound[0]:
            self.rect.left = self.bound[0]

    def Moveright(self):
        if self.rect.right + self.movespeed <= self.bound[1]:
            self.rect.right += self.movespeed
        elif self.rect.right + self.movespeed > self.bound[1]:
            self.rect.right = self.bound[1]
            
    def Moveup(self):
        if  self.rect.top - self.movespeed >= self.bound[2]:
            self.rect.top -= self.movespeed
        elif self.rect.top - self.movespeed < self.bound[2]:
            self.rect.top = self.bound[2]

    def Movedown(self):
        if  self.rect.bottom + self.movespeed <= self.bound[3]:
            self.rect.bottom += self.movespeed
        elif self.rect.bottom + self.movespeed > self.bound[3]:
            self.rect.bottom = self.bound[3]
 
def main():
    global screen
    pygame.init()
    
    ShowCell=False

    cell_width=screen_width/11
    cell_height=(screen_height-400)/3

    FPSCLOCK = pygame.time.Clock()
    screen.fill(pygame.Color('white'))
    backgrImage = pygame.image.load('Back.jpg')
    backgrImage = pygame.transform.scale(backgrImage, (screen_width, screen_height-400))
    screen.blit(backgrImage, [0,0])

    Man = man( (50,100), (0, screen_width, 0, screen_height-400))
    screen.blit(Man.image, Man.rect)    

    pygame.display.update()

    while True:


        screen.blit(backgrImage, [0,0])
        keys = pygame.key.get_pressed()
        (x,y)=Man.rect.left, Man.rect.top
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    terminate()
                # Press return button will get the photo.if event.key == pygame.K_RETURN:

                #First row 0_0----10_0
                if event.key == pygame.K_RETURN:                
                    if x > 0 and x < 1*cell_width and y > 0 and y < 1*cell_height:
                        unit_image = pygame.image.load('Pictures/' + '0_0.png')
                        screen.blit(unit_image, [845,540])
                    if x > 1*cell_width and x < 2*cell_width and y > 0 and y < 1*cell_height:
                        unit_image = pygame.image.load('Pictures/' + '1_0.png')
                        screen.blit(unit_image, [845,540])
                    if x > 2*cell_width and x < 3*cell_width and y > 0 and y < 1*cell_height:
                        unit_image = pygame.image.load('Pictures/' + '2_0.png')
                        screen.blit(unit_image, [845,540])
                    if x > 3*cell_width and x < 4*cell_width and y > 0 and y < 1*cell_height:
                        unit_image = pygame.image.load('Pictures/' + '3_0.png')
                        screen.blit(unit_image, [845,540])
                    if x > 4*cell_width and x < 5*cell_width and y > 0 and y < 1*cell_height:
                        unit_image = pygame.image.load('Pictures/' + '4_0.png')
                        screen.blit(unit_image, [845,540])
                    if x > 5*cell_width and x < 6*cell_width and y > 0 and y < 1*cell_height:
                        unit_image = pygame.image.load('Pictures/' + '5_0.png')
                        screen.blit(unit_image, [845,540])
                    if x > 6*cell_width and x < 7*cell_width and y > 0 and y < 1*cell_height:
                        unit_image = pygame.image.load('Pictures/' + '6_0.png')
                        screen.blit(unit_image, [845,540])
                    if x > 7*cell_width and x < 8*cell_width and y > 0 and y < 1*cell_height:
                        unit_image = pygame.image.load('Pictures/' + '7_0.png')
                        screen.blit(unit_image, [845,540])
                    if x > 8*cell_width and x < 9*cell_width and y > 0 and y < 1*cell_height:
                        unit_image = pygame.image.load('Pictures/' + '8_0.png')
                        screen.blit(unit_image, [845,540])
                    if x > 9*cell_width and x < 10*cell_width and y > 0 and y < 1*cell_height:
                        unit_image = pygame.image.load('Pictures/' + '9_0.png')
                        screen.blit(unit_image, [845,540])
                    if x > 10*cell_width and x < 11*cell_width and y > 0 and y < 1*cell_height:
                        unit_image = pygame.image.load('Pictures/' + '10_0.png')
                        screen.blit(unit_image, [845,540])


                    #Second row 0_1----10_1

                    if x > 0 and x < 1*cell_width and y > 1*cell_height and y < 2*cell_height:
                        unit_image = pygame.image.load('Pictures/' + '0_1.png')
                        screen.blit(unit_image, [845,540])
                    if x > 1*cell_width and x < 2*cell_width and y > 1*cell_height and y < 2*cell_height:
                        unit_image = pygame.image.load('Pictures/' + '1_1.png')
                        screen.blit(unit_image, [845,540])
                    if x > 2*cell_width and x < 3*cell_width and y > 1*cell_height and y < 2*cell_height:
                        unit_image = pygame.image.load('Pictures/' + '2_1.png')
                        screen.blit(unit_image, [845,540])
                    if x > 3*cell_width and x < 4*cell_width and y > 1*cell_height and y < 2*cell_height:
                        unit_image = pygame.image.load('Pictures/' + '3_1.png')
                        screen.blit(unit_image, [845,540])
                    if x > 4*cell_width and x < 5*cell_width and y > 1*cell_height and y < 2*cell_height:
                        unit_image = pygame.image.load('Pictures/' + '4_1.png')
                        screen.blit(unit_image, [845,540])
                    if x > 5*cell_width and x < 6*cell_width and y > 1*cell_height and y < 2*cell_height:
                        unit_image = pygame.image.load('Pictures/' + '5_1.png')
                        screen.blit(unit_image, [845,540])
                    if x > 6*cell_width and x < 7*cell_width and y > 1*cell_height and y < 2*cell_height:
                        unit_image = pygame.image.load('Pictures/' + '6_1.png')
                        screen.blit(unit_image, [845,540])
                    if x > 7*cell_width and x < 8*cell_width and y > 1*cell_height and y < 2*cell_height:
                        unit_image = pygame.image.load('Pictures/' + '7_1.png')
                        screen.blit(unit_image, [845,540])
                    if x > 8*cell_width and x < 9*cell_width and y > 1*cell_height and y < 2*cell_height:
                        unit_image = pygame.image.load('Pictures/' + '8_1.png')
                        screen.blit(unit_image, [845,540])
                    if x > 9*cell_width and x < 10*cell_width and y > 1*cell_height and y < 2*cell_height:
                        unit_image = pygame.image.load('Pictures/' + '9_1.png')
                        screen.blit(unit_image, [845,540])
                    if x > 10*cell_width and x < 11*cell_width and y > 1*cell_height and y < 2*cell_height:
                        unit_image = pygame.image.load('Pictures/' + '10_1.png')
                        screen.blit(unit_image, [845,540])


                    #Third row 0_2----10_2

                    if x > 0 and x < 1*cell_width and y > 2*cell_height and y < 3*cell_height:
                        unit_image = pygame.image.load('Pictures/' + '0_2.png')
                        screen.blit(unit_image, [845,540])
                    if x > 1*cell_width and x < 2*cell_width and y > 2*cell_height and y < 3*cell_height:
                        unit_image = pygame.image.load('Pictures/' + '1_2.png')
                        screen.blit(unit_image, [845,540])
                    if x > 2*cell_width and x < 3*cell_width and y > 2*cell_height and y < 3*cell_height:
                        unit_image = pygame.image.load('Pictures/' + '2_2.png')
                        screen.blit(unit_image, [845,540])
                    if x > 3*cell_width and x < 4*cell_width and y > 2*cell_height and y < 3*cell_height:
                        unit_image = pygame.image.load('Pictures/' + '3_2.png')
                        screen.blit(unit_image, [845,540])
                    if x > 4*cell_width and x < 5*cell_width and y > 2*cell_height and y < 3*cell_height:
                        unit_image = pygame.image.load('Pictures/' + '4_2.png')
                        screen.blit(unit_image, [845,540])
                    if x > 5*cell_width and x < 6*cell_width and y > 2*cell_height and y < 3*cell_height:
                        unit_image = pygame.image.load('Pictures/' + '5_2.png')
                        screen.blit(unit_image, [845,540])
                    if x > 6*cell_width and x < 7*cell_width and y > 2*cell_height and y < 3*cell_height:
                        unit_image = pygame.image.load('Pictures/' + '6_2.png')
                        screen.blit(unit_image, [845,540])
                    if x > 7*cell_width and x < 8*cell_width and y > 2*cell_height and y < 3*cell_height:
                        unit_image = pygame.image.load('Pictures/' + '7_2.png')
                        screen.blit(unit_image, [845,540])
                    if x > 8*cell_width and x < 9*cell_width and y > 2*cell_height and y < 3*cell_height:
                        unit_image = pygame.image.load('Pictures/' + '8_2.png')
                        screen.blit(unit_image, [845,540])
                    if x > 9*cell_width and x < 10*cell_width and y > 2*cell_height and y < 3*cell_height:
                        unit_image = pygame.image.load('Pictures/' + '9_2.png')
                        screen.blit(unit_image, [845,540])
                    if x > 10*cell_width and x < 11*cell_width and y > 2*cell_height and y < 3*cell_height:
                        unit_image = pygame.image.load('Pictures/' + '10_2.png')
                        screen.blit(unit_image, [845,540])


        if keys[K_ESCAPE]:
            terminate()
        if keys[K_a] or keys[K_LEFT]:
            Man.Moveleft()     
        if keys[K_d] or keys[K_RIGHT]:
            Man.Moveright()
        if keys[K_s] or keys[K_DOWN]:
            Man.Movedown()
        if keys[K_w] or keys[K_UP]:
            Man.Moveup()       
            
        screen.blit(Man.image, Man.rect)
                    
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def terminate():
    pygame.quit()
    sys.exit()

if  __name__ == '__main__':
    main()


pygame.display.update()
