import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 480

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0, 200, 0)
bright_green = (0, 255, 0)
bright_red = (255,0,0)

mouse_width = 100
mouse_speed = 6

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Mouse_Trap')
clock = pygame.time.Clock()

mouseImg = pygame.image.load('mouse.png')
trapImg = pygame.image.load('trap.jpg')

pause = False

	
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pygame.font.Font('AGENCYR.TTF',85)
        TextSurf, TextRect = text_objects("Welcome to Mouse Trap!", largeText)
        TextRect.center = ((display_width/2),(display_height/4))
        gameDisplay.blit(TextSurf, TextRect)

        largeText = pygame.font.Font('AGENCYR.TTF',45)
        TextSurf, TextRect = text_objects("Score more than 15 to prove sobriety", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
		
        button("Start",350,450,100,50,green,bright_green,game_loop)

      
        pygame.display.update()
        clock.tick(15)


def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))

def things(thingx, thingy, thingw, thingh):
    gameDisplay.blit(trapImg,(thingx, thingy, thingw, thingh))

	
def mouse(x,y):
    gameDisplay.blit(mouseImg,(x,y))


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('CHLORINR_0.TTF',105)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(4)
    
    pygame.quit()

def quitgame():
    crash ()


def crash():
    message_display('GGWP MAN')
    

	
def button(msg,x,y,w,h,ic,ac,action=None):
    mice = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
	
	
    if 350+100 > mice[0] > 350 and 350+50 > mice[1] > 350:
        pygame.draw.rect(gameDisplay, bright_green,(350,350,100,50))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, green,(350,350,100,50))

    smallText = pygame.font.Font("coffee.ttf",20)
    textSurf, textRect = text_objects("Start", smallText)
    textRect.center = ( (350+(100/2)), (350+(50/2)) )
    gameDisplay.blit(textSurf, textRect)
	
def buttonA(msg,x,y,w,h,ic,ac,action=None):
    mice = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
	
    if 350+100 > mice[0] > 350 and 350+50 > mice[1] > 350:
        pygame.draw.rect(gameDisplay, bright_green,(350,350,100,50))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, green,(350,350,100,50))

    smallText = pygame.font.Font("coffee.ttf",20)
    textSurf, textRect = text_objects("Continue", smallText)
    textRect.center = ( (350+(100/2)), (350+(50/2)) )
    gameDisplay.blit(textSurf, textRect)
	
def unpause():
	global pause
	pause = False

def paused():

    while pause:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pygame.font.Font("AGENCYR.TTF",115)
        TextSurf, TextRect = text_objects("Paused", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

		
        buttonA("Continue",150,450,100,50,green,bright_green,unpause)


        pygame.display.update()
        clock.tick(15)
					

def game_loop():
    global pause

    x = (display_width * 0.45)
    y = (display_height * 0.75)

    x_change = 0

    mouse_speed = 8
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 4
    thing_width = 85
    thing_height = 100

    thingCount = 1

    dodged = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_p:
                    pause = True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
					
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    x = pygame.mouse.get_pos()[0]


        pos = pygame.mouse.get_pos()
        x = pos[0]
        b = pos[1]

        mouse(x,b)
	
        x += x_change
        gameDisplay.fill(white)

        # things(thingx, thingy, thingw, thingh)
        things(thing_startx, thing_starty, thing_width, thing_height)
        
        thing_starty += thing_speed
        mouse(x,y)
        things_dodged(dodged)

        if x > display_width - mouse_width or x < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
            dodged += 1
            thing_speed += 0.80
            mouse_speed += 1

        if y < thing_starty+thing_height:
            #print('y crossover')

            if x > thing_startx and x < thing_startx + thing_width or x+mouse_width > thing_startx and x + mouse_width < thing_startx+thing_width:
                #print('x crossover')
                crash()
        
        pygame.display.update()
        clock.tick(60)

if __name__=='__main__':
	game_intro()
	game_loop()
	pygame.quit()
	quit()
