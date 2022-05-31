#-----------------------------------------------------------------------------------------Imports
import pygame
import time
import random

#-----------------------------------------------------------------------------------------Game speed
snakeSpeed = 15

#-----------------------------------------------------------------------------------------Game Window
winX = 720
winY = 480

#-----------------------------------------------------------------------------------------Define Colours
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

#-----------------------------------------------------------------------------------------Initialising PyGame and window
pygame.init()
pygame.display.set_caption('Snake game trial 4')
win = pygame.display.set_mode((winX, winY))
fps = pygame.time.Clock()
snakePos = [100, 50]
snakeBody = [[100, 50], [90, 50], [80, 50], [70, 50]]
foodPos = [random.randrange(1, (winX//10))*10, random.randrange(1, (winY//10))*10]
foodSpawn = True

#-----------------------------------------------------------------------------------------Snake default characteristics
direction = 'RIGHT'
changeDir = direction

#-----------------------------------------------------------------------------------------Scores
score = 0
def showScore(choice, color, font, size=20):
    scoreFont = pygame.font.SysFont(font, size)                                             # Creating a font for the score
    scoreSurface = scoreFont.render('Score : ' + str(score), True, color)                      # Surface on which the score will be displayed
    scoreRect = scoreSurface.get_rect()                                                      # Rect surface for displaying score
    win.blit(scoreSurface, scoreRect)

def GameOver():
    myfont = pygame.font.SysFont('times new roman', 50)                                 # Creating a font style for Game Over message
    GameOverSurface = myfont.render('Your score is : ' + str(score), True, red)            # Surface over which game over will display
    GameOverRect = GameOverSurface.get_rect()                                           # Get a rectangle for the message
    GameOverRect.midtop = (winX/2, winY/4)                                             # Setting position of the text
    win.blit(GameOverSurface, GameOverRect)                                              # Draw the text on the screen
    pygame.display.flip()
    time.sleep(3)                                                                          # exit the game after 3 sec
    pygame.quit()                                                                         # Deactivating PyGame library
    quit()                                                                                 # Quit the program

#-----------------------------------------------------------------------------------------Main Function
while True:
    for event in pygame.event.get():                                                      # Controls for the Game
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_UP :
                changeDir = 'UP'
            if event.key == pygame.K_DOWN :
                changeDir = 'DOWN'
            if event.key == pygame.K_LEFT :
                changeDir = 'LEFT'
            if event.key == pygame.K_RIGHT :
                changeDir = 'RIGHT'
    
    #-----------------------------------------------------------------------------------------To remove confusion between two keys pressed together
    if changeDir == 'UP' and direction != 'DOWN' :
        direction = 'UP'
    if changeDir == 'DOWN' and direction != 'UP' :
        direction = 'DOWN'
    if changeDir == 'LEFT' and direction != 'RIGHT' :
        direction = 'LEFT'
    if changeDir == 'RIGHT' and direction != 'LEFT' :
        direction = 'RIGHT'
    
    #-----------------------------------------------------------------------------------------Moving the snake with Controls
    if direction == 'UP' :
        snakePos[1] -= 10
    if direction == 'DOWN' :
        snakePos[1] += 10
    if direction == 'LEFT' :
        snakePos[0] -= 10
    if direction == 'RIGHT' :
        snakePos[0] += 10
    
    #-----------------------------------------------------------------------------------------Body block increament
    snakeBody.insert(0, list(snakePos))
    if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1] :
        score += 10
        foodSpawn = False
    else :
        snakeBody.pop()
    
    if not foodSpawn:
        foodPos = [random.randrange(1, (winX//10))*10, random.randrange(1, (winY//10))*10]
    
    foodSpawn = True
    win.fill(black)

    for pos in snakeBody:
        pygame.draw.rect(win, green, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(win, white, pygame.Rect(foodPos[0], foodPos[1], 10, 10))

    #-----------------------------------------------------------------------------------------Game Over Conditions
    if snakePos[0] < 0 or snakePos[0] > winX-10 :
        GameOver()
    if snakePos[1] < 0 or snakePos[1] > winY - 10 :
        GameOver()
    
    #-----------------------------------------------------------------------------------------Touching snake body
    for block in snakeBody[1:] :
        if snakePos[0] == block[0] and snakePos[1] == block[1] :
            GameOver()
    
    #-----------------------------------------------------------------------------------------Continous score
    showScore(1, white, 'times new roman', 20)

    #-----------------------------------------------------------------------------------------Refresh Game screen
    pygame.display.update()

    #-----------------------------------------------------------------------------------------Refresh rate or Frames Per Second
    fps.tick(snakeSpeed)