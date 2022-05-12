import pygame,sys
import random

# Define Game parameters
# screen size
screen_width=1890
screen_height=940
bound = (0, 0, screen_width, screen_height-400)
# grid selection
xSel =0
ySel =0
#Boolean for showing cells
ShowCell=False

# initialise the game window
pygame.init()
pygame.display.set_caption("Blind box extraction")

# set the game surface
screen=pygame.display.set_mode((screen_width,screen_height))

# a clock to keep track of the game progress
clock = pygame.time.Clock()

screen.fill(pygame.Color('white'))

backgrImage = pygame.image.load('back.jpg')
backgrImage = pygame.transform.scale(backgrImage, (screen_width, screen_height-400))
screen.blit(backgrImage, [0,0])
pygame.display.update()

square =[]
for i in range(11):
    row=[]
    for j in range(3):
        r=pygame.Rect(i*(screen_width/11),j*((screen_height-400)/3),
        screen_width/11,(screen_height-400)/3)
        row.append(r)
    square.append(row)  

while True:
    screen.blit(backgrImage, [0,0])
    events=pygame.event.get()
    for event in events:
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_RIGHT:
                if xSel < 10:
                    xSel +=1
            if event.key == pygame.K_LEFT:
                if xSel > 0:
                    xSel -=1
            if event.key == pygame.K_UP:
                if ySel > 0:
                    ySel -= 1
            if event.key == pygame.K_DOWN:
                if ySel < 2:
                    ySel += 1
            if event.key == pygame.K_RETURN:
                if ShowCell:
                    ShowCell = False
                else:
                    ShowCell = True

  
    pygame.draw.rect(screen, pygame.Color("pink"), square[xSel][ySel])

    if ShowCell:
        try:
            cellImage = pygame.image.load('Pictures/' + str(xSel) + '_' + str(ySel) + '.png')
           
            screen.blit(cellImage, [845,540])
        except FileNotFoundError:
            ShowCell = False

    # At the end of the loop update the screen and game time.    
    pygame.display.update()
    clock.tick()