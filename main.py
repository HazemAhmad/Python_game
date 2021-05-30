import pygame
import time
import random


pygame.init()

display_width = 1000
display_height = 800
black = (0, 0, 0)
white = (255, 255, 255)
red = (150, 0, 0)
bright_red = (255, 0, 0)
green = (0, 150, 0)
bright_green = (0, 255, 0)
obstacle_color = (180, 240, 90)

carImg = pygame.image.load('plane.png')
plane_width = 68  # depends of the imensions of the object used
gameDisplay = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()


def obstacles_dodged(count):
    font = pygame.font.SysFont(None, '35')
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text, (0, 0))


def obstacles(obstaclex, obstacley, obstaclew, obstacleh, color):
    pygame.draw.rect(gameDisplay, color, [
                     obstaclex, obstacley, obstaclew, obstacleh])


def car(x, y):
    gameDisplay.blit(carImg, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    textSurf, textRect = text_objects(text, largeText)
    textRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(textSurf, textRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()


def crash():
    message_display('You crashed!')


def button(msg, x, y, w, h, inactive_col, active_col):
    mouse = pygame.mouse.get_pos()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, active_col, (x, y, w, h))
    else:
        pygame.draw.rect(gameDisplay, inactive_col, (x, y, w, h))

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    gameDisplay.blit(textSurf, textRect)


def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        textSurf, textRect = text_objects("Race and Crash", largeText)
        textRect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(textSurf, textRect)
        button("Start!", 150, 650, 100, 50, green, bright_green)
        button("Quit!", 750, 650, 100, 50, red, bright_red)
        pygame.display.update()
        clock.tick(15)
        time.sleep(2)
        intro = False


def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    obstacle_startx = random.randrange(0, display_width)
    obstacle_starty = -600
    obstacle_speed = 7
    obstacle_width = 100
    obstacle_height = 100

    x_change = 0
    y_change = 0
    game_score = 0

    pygame.display.set_caption('Race and Crash')
    clock = pygame.time.Clock()
    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                elif event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

        x += x_change
        y += y_change
        gameDisplay.fill(white)

        obstacles(obstacle_startx, obstacle_starty,
                  obstacle_width, obstacle_height, obstacle_color)
        obstacle_starty += obstacle_speed
        car(x, y)
        # obstacles_dodged(game_score)
        font = pygame.font.SysFont(None, 25)
        text = font.render("Dodged: "+str(game_score), True, black)
        gameDisplay.blit(text, (0, 0))

        if x > display_width - plane_width or x < 0:
            crash()
        if obstacle_starty > display_height:
            obstacle_starty = 0 - obstacle_height
            obstacle_startx = random.randrange(0, display_width)
            game_score += 1
            # obstacle_speed += 1
            obstacle_width += (game_score * 1.8)

        if y < obstacle_starty + obstacle_height:
            # print('y crossove')
            if (x > obstacle_startx and x < obstacle_startx + obstacle_width or
                    x + plane_width > obstacle_startx and x +
                    plane_width < obstacle_startx + obstacle_width):
                # print('x_crossover')
                crash()

        pygame.display.update()
        clock.tick(60)


game_intro()
game_loop()
pygame.quit()
quit()
