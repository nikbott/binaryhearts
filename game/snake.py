# This minigame will be incorporated to the visual novel "Binary Hearts". It consists of a snake game in which the player must continue until
# a certain amount of consecutive red fruits is eaten. Each new thought to be eaten will have a random color, and the difficulty will increase
# as the number of eaten reds grow in the 2^x formula. 

# Furthermore in the game we plan to make this minigame infinite, where you can only quit by winning, and if the player loses, they start
# over again. Also, the number of failures will determine further lore of the main game.

# Pedro Augusto Faria    - 821124
# Vinicius Machado Daros - 
# Vinicius Reyes Kury    - 819730

# importing libraries
import sys, pygame, time, random
from pygame.locals import *
import random

# Window size
window_WIDTH = 800 # X axis size
window_HEIGHT = 600 # Y axis size


#########################################################################################

# queue functions implementation with five primitives

def queue_create(): # creates an empty queue
    return [] # returns an empty list


def enqueue(q: list, item): # adds an item to the queue
    q.append(item) # adds the item to the end of the list


def queue_empty(q: list): # checks if the queue is empty 
    return True if not q else False # returns True if the queue is empty, False otherwise


def dequeue(q: list): # removes an item from the queue
    if queue_empty(q): # checks if the queue is empty
        assert False, 'Queue is empty' # if the queue is empty, raises an error
    return q.pop(0) # returns the first item of the list


def queue_full(q: list): # checks if the queue is full
    return False # returns False, since the queue is never full


#########################################################################################


#          R    G    B 
black  = (  0,   0,   0) 
white  = (255, 255, 255)
red    = (255,   0,   0)
green  = (  0, 255,   0)
blue   = (  0,   0, 255)
purple = (138,  43, 226)
yellow = (255, 255,   0)

# pygame initialization
pygame.init() 

# FPS var
FPS = 20 

# main game surface object initialization
pygame.display.set_caption('Snake Minigame for AED1')  # title of the game
game_window = pygame.display.set_mode((window_WIDTH, window_HEIGHT)) # size of the game window

# FPS Clock object initialization
fps = pygame.time.Clock()  # clock object to track time 

# defining snake default position
snake_position = [100, 20] # snake position at the beginning of the game

# first block of snake body
snake_body = [[100, 20], [90, 20], [80, 20],] # snake body at the beginning of the game

# snake colors
snake_colors = [green, green, green,] # snake colors at the beginning of the game

# thought position
thought_position = [random.randrange(1, (window_WIDTH // 10)) * 10, 
                  random.randrange(1, (window_HEIGHT // 10)) * 10]  # thought position at the beginning of the game

thought_spawn = True # boolean to check if the thought is spawned

#  snake direction (right)
direction = 'RIGHT'
change_to = direction

# score intialization
thoughts_eaten = 0 # score at the beginning of the game


#########################################################################################


# generates a random color
def rand_color():
    i = random.randint(1, 10) # generates a random number between 1 and 10
    if 1 <= i <= 5: # if the number is between 1 and 5, returns red
        return red 
    elif i == 6: # if the number is 6, returns green
        return green
    elif i == 7: # if the number is 7, returns blue
        return blue
    elif i == 8 or i == 10: # if the number is 8 or 10, returns purple
        return purple
    elif i == 9: # if the number is 9, returns yellow
        return yellow


#########################################################################################


# displaying Score function
def show_score(choice, color, font, size): # choice = 1 for game over and 0 for play

    score_font = pygame.font.SysFont(font, size) # font type and size

    # create the surface object
    score_surface = score_font.render('Thoughts Eaten : ' + str(thoughts_eaten), True, color) # text and color

    # create a rectangular object for the text surface object
    score_rect = score_surface.get_rect()

    # blit will draw the text on screen
    game_window.blit(score_surface, score_rect) 


#########################################################################################


def you_win(): # game winning function

    my_font = pygame.font.SysFont('helvetica', 25) # font type and size

    # creating a text surface on which text
    game_winning_surface = my_font.render(
        'You\'ve won your own mind!', True, green)

    # create a rectangular object for the text
    game_winning_rect = game_winning_surface.get_rect()

    # text location
    game_winning_rect.midtop = (window_WIDTH / 2, window_HEIGHT / 4)

    # blit will draw the text on screen
    game_window.blit(game_winning_surface, game_winning_rect)
    pygame.display.flip()

    # two seconds delay
    time.sleep(2)

    # library deactivation
    pygame.quit()

    # program quit
    quit()


####################################################################################

# function for game over
def game_over():

    my_font = pygame.font.SysFont('helvetica', 25) 

    # creating a text surface on which text
    game_over_surface = my_font.render(
        'You\'ve eaten ' + str(thoughts_eaten) + ' thoughts.. But that\'s not enough..', True, red)

    # create a rectangular object for the text
    game_over_rect = game_over_surface.get_rect()

    # text location
    game_over_rect.midtop = (window_WIDTH / 2, window_HEIGHT / 4)

    # for displaying the text 
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    # delay of two seconds
    time.sleep(2)

    # deactivation of the library
    pygame.quit()

    # quiting the program
    quit()


###########################################################################################


# thought color
new_color = rand_color()

# size of snake and thought
size = 10

# queue for the evaluation, with three greens at start
q1 = queue_create()
enqueue(q1, green)
enqueue(q1, green)
enqueue(q1, green)



###########################################################################################


# Main Function
while True:

    # handling events for the movement of the snake
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
            if event.key == pygame.K_LSHIFT: # if the left shift is pressed, the FPS is doubled, like a sprint function
                FPS = 60

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LSHIFT:
                FPS = 30

    # validating the direction
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # changing the snake position
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10


###############################################################################

    # snake body mechanism
    snake_body.insert(0, list(snake_position)) # inserts a new block in the snake body

    if thoughts_eaten == 0: # if the snake has eaten no thoughts, the color of the new block is set for an initial value
        past_color = new_color

    if snake_position[0] == thought_position[0] and snake_position[1] == thought_position[1]: # if the snake eats a thought

        past_color = new_color # the color of the new block is set to the color of the thought
        snake_colors.append(past_color) # the color of the new block is added to the list of colors
        enqueue(q1, past_color) # the color of the new block is added to the queue
        new_color = rand_color() # a new color is generated for the thought
        thought_spawn = False # the thought is not spawned
        thoughts_eaten += 1 # the score is incremented

    else:
        snake_body.pop() # if the snake doesn't eat a thought, the last block of the snake body is removed

    if not thought_spawn:
        thought_position = [random.randrange(1, (window_WIDTH // 10)) * 10,
                          random.randrange(1, (window_HEIGHT // 10)) * 10] # if the thought is not spawned, a new position is generated

    thought_spawn = True # the thought is spawned
    game_window.fill(black) # the game window is filled with black

    # snake body generator
    i = 0 # counter for the colors
    for pos in snake_body: # for each block of the snake body
        pygame.draw.rect(game_window, snake_colors[i], pygame.Rect(pos[0], pos[1], size, size)) # a rectangle is drawn with the color of the block
        i += 1 # the counter is incremented

    # evaluation for the game end
    t = 0 # counter for the queue
    temp = list(q1) # temporary list for the queue

    while not queue_empty(temp): # while the queue is not empty
        color = dequeue(temp) # the first color of the queue is removed
        
        if t == 0 and color == red: # if the first color is red, the counter is incremented
            t += 1
        elif t == 1 and color != red: # if the second color is not red, the counter is reset
            t = 0
        elif t == 1 and color == red: # if the second color is red, the counter is incremented
            t += 1
        elif t == 2 and color != red: # if the third color is not red, the counter is reset
            t = 0
        elif t == 2 and color == red: # if the third color is red, the counter is incremented
            t += 1
        if t == 3: # if the counter is 2, the game is over
            you_win() # the game winning function is called


    # new thought generator
    pygame.draw.rect(game_window, new_color, pygame.Rect( 
        thought_position[0], thought_position[1], size, size))  # draws a rectangle with the color of the thought


##################################################################################

    # evaluating the end of the game

    # if the snake touch the walls
    if snake_position[0] < 0 or snake_position[0] > window_WIDTH - 10: # if the snake touches the left or right wall
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_HEIGHT - 10: # if the snake touches the top or bottom wall
        game_over()

    # if the snake touch itself
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]: # if the snake touches itself
            game_over()

    # score display showoff
    show_score(1, green, 'helvetica', 30)

    # game state update
    pygame.display.update()

    # clock type object tick based on 'frame rate'
    fps.tick(FPS)
