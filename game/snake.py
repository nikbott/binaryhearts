import sys, pygame, time, random
from pygame.locals import *

BLACK  = (  0,   0,   0) 
RED    = (255,   0,   0)
GREEN  = (  0, 255,   0)
BLUE   = (  0,   0, 255)
PURPLE = (138,  43, 226)
YELLOW = (255, 255,   0)

WIDTH = 640
HEIGHT = 640

def queue_create():
    """
    Creates an empty queue.

    Returns:
        list: An empty list representing the queue.
    """
    return []


def enqueue(q: list, item):
    """
    Adds an item to the queue.

    Parameters:
    q (list): The queue to add the item to.
    item: The item to be added to the queue.
    """
    q.append(item)


def queue_empty(q: list):
    """
    Checks if the queue is empty.

    Args:
        q (list): The queue to be checked.

    Returns:
        bool: True if the queue is empty, False otherwise.
    """
    return True if not q else False


def dequeue(q: list):
    """
    Removes an item from the queue.

    Args:
        q (list): The queue from which to remove an item.

    Returns:
        The first item of the queue.

    Raises:
        AssertionError: If the queue is empty.
    """
    if queue_empty(q):
        assert False, 'Queue is empty'
    return q.pop(0)


def queue_full(q: list):
    """
    Checks if the queue is full.

    Args:
        q (list): The queue to be checked.

    Returns:
        bool: True if the queue is full, False otherwise.
    """
    return False


def rand_color():
    i = random.randint(1, 10)
    if 1 <= i <= 5:
        return RED 
    elif i == 6:
        return GREEN
    elif i == 7:
        return BLUE
    elif i == 8 or i == 10:
        return PURPLE
    elif i == 9:
        return YELLOW


def show_score(screen, score):
    score_font = pygame.font.SysFont('helvetica', 30)

    # create the surface object
    score_surface = score_font.render('Thoughts Eaten : ' + str(score), True, GREEN) # text and color

    # create a rectangular object for the text surface object
    score_rect = score_surface.get_rect()

    # blit will draw the text on screen
    screen.blit(score_surface, score_rect) 


def you_win(screen):
    my_font = pygame.font.SysFont('helvetica', 25)

    game_winning_surface = my_font.render(
        'You\'ve won your own mind!', True, GREEN)
    game_winning_rect = game_winning_surface.get_rect()

    # text location
    game_winning_rect.midtop = (WIDTH / 2, HEIGHT / 4)

    screen.blit(game_winning_surface, game_winning_rect)
    pygame.display.flip()

    time.sleep(2)
    pygame.quit()
    quit()


def game_over(screen, score):
    my_font = pygame.font.SysFont('helvetica', 25) 

    game_over_surface = my_font.render(
        'You\'ve eaten ' + str(score) + ' thoughts.. But that\'s not enough..', True, RED)
    game_over_rect = game_over_surface.get_rect()

    # text location
    game_over_rect.midtop = (WIDTH / 2, HEIGHT / 4)

    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    time.sleep(2)
    pygame.quit()
    quit()


def main():
    #screen = pygame.Surface((WIDTH, HEIGHT))

    # initial values

    FPS = 20
    direction = 'RIGHT'
    change_to = direction
    score = 0
    snake_position = [100, 20]
    snake_body = [[100, 20], [90, 20], [80, 20]]
    snake_colors = [GREEN, GREEN, GREEN]
    thought_position = [random.randrange(1, (WIDTH // 10)) * 10, 
                    random.randrange(1, (HEIGHT // 10)) * 10]
    thought_spawn = True # boolean to check if the thought is spawned
    new_color = rand_color() # thought color
    size = 10 # size of snake and thought

    q1 = queue_create() # queue for the evaluation, with three greens at start
    enqueue(q1, GREEN)
    enqueue(q1, GREEN)
    enqueue(q1, GREEN)

    # initialize pygame
    pygame.init() 
    screen = pygame.display.set_mode((WIDTH, HEIGHT)) # game window
    fps = pygame.time.Clock() # FPS Clock object initialization

    while True:
        # handling events for the movement of the snake
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
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
                if event.key == pygame.K_LSHIFT: # if lshift is pressed, FPS is doubled
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

        snake_body.insert(0, list(snake_position))

        # if the snake has eaten no thoughts, the color of the new block is set for an initial value
        if score == 0:
            past_color = new_color

        # if the snake eats a thought
        if snake_position[0] == thought_position[0] and snake_position[1] == thought_position[1]:
            past_color = new_color # the color of the new block is set to the color of the thought
            snake_colors.append(past_color) # the color of the new block is added to the list of colors
            enqueue(q1, past_color) # the color of the new block is added to the queue
            new_color = rand_color() # a new color is generated for the thought
            thought_spawn = False
            score += 1
        else:
            snake_body.pop() # if the snake doesn't eat a thought, the last block of the snake body is removed

        if not thought_spawn:
            thought_position = [random.randrange(1, (WIDTH // 10)) * 10,
                            random.randrange(1, (HEIGHT // 10)) * 10] # if the thought is not spawned, a new position is generated

        thought_spawn = True
        screen.fill(BLACK)

        # snake body generator
        i = 0 # counter for the colors
        for pos in snake_body:
            pygame.draw.rect(screen, snake_colors[i], pygame.Rect(pos[0], pos[1], size, size)) # a rectangle is drawn with the color of the block
            i += 1

        t = 0 # counter for the queue
        temp = list(q1) # temporary list for the queue

        # if the queue has three reds in a row, the game ends
        while not queue_empty(temp):
            color = dequeue(temp)
            if t == 0 and color == RED:
                t += 1
            elif t == 1 and color != RED:
                t = 0
            elif t == 1 and color == RED:
                t += 1
            elif t == 2 and color != RED:
                t = 0
            elif t == 2 and color == RED:
                t += 1
            if t == 3:
                you_win(screen)

        # draws a rectangle with the color of the thought
        pygame.draw.rect(screen, new_color, pygame.Rect( 
            thought_position[0], thought_position[1], size, size))

        # if the snake touch the walls
        if snake_position[0] < 0 or snake_position[0] > WIDTH - 10: # left or right wall
            game_over(screen, score)
        if snake_position[1] < 0 or snake_position[1] > HEIGHT - 10: # top or bottom wall
            game_over(screen, score)

        # if the snake touches itself
        for block in snake_body[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                game_over(screen, score)

        show_score(screen, score)

        pygame.display.update()
        fps.tick(FPS)

if __name__ == '__main__':
    main()
