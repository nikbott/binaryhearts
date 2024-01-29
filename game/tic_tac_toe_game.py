import pygame
import random
import sys
import os

# Initialize the mixer module
# pygame.mixer.init()

# Define the AI fail rate for the difficulty; 0 means the AI is unbeatable, 1 means the AI is stupid; 0.2 is a good value;
AI_FAIL_RATE = 0.2

WIDTH, HEIGHT = 700, 700
#WIDTH2, HEIGHT2 = 1366, 768
LINE_WIDTH = 15
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS

# win and lose sounds
rectangle = False

# background = 'soundtrack.mp3'
# win_sound = pygame.mixer.Sound(os.path.join('win.mp3'))
# lose_or_tie_sound = pygame.mixer.Sound(os.path.join('lose.mp3'))

# Load and play the music
# pygame.mixer.music.load(background)
# pygame.mixer.music.play(-1)

# Colors
BG_COLOR = (0, 0, 0)
LINE_COLOR = (173, 216, 255)
X_COLOR = (173, 216, 255)
O_COLOR = (173, 216, 255)
RESULT_BOX_COLOR = (0, 170, 0)

# Class Node for the minimax algorithm
class Node:
    """
    Represents a node in the minimax algorithm tree.

    Attributes:
    - board: The current state of the game board.
    - depth: The depth of the node in the tree.
    - is_maximizing: A boolean indicating whether the node is
    maximizing or minimizing.
    - children: A list of child nodes.
    """

    def __init__(self, board, depth, is_maximizing):
        """
        Initializes a new Node object.

        Parameters:

        - board: The current state of the game board.
        - depth: The depth of the node in the tree.
        - is_maximizing: A boolean indicating whether the node is
        maximizing or minimizing.
        """

        self.board = board
        self.depth = depth
        self.is_maximizing = is_maximizing
        self.children = []

    def generate_children(self):
        """
        Generates all possible child nodes for the current node.
        """

        for i in range(BOARD_ROWS):
            for j in range(BOARD_COLS):
                if self.board[i][j] == ' ':
                    new_board = [row.copy() for row in self.board]
                    new_board[i][j] = 'O' if self.is_maximizing else 'X'
                    self.children.append(Node(new_board, self.depth + 1, not self.is_maximizing))

    def insert_node(self, new_node):
        """
        Inserts a new node into the list of children nodes.

        Parameters:
        - new_node: The node to be inserted.
        """

        for child in self.children:
            if child.board == new_node.board:
                return # Node already exists
        self.children.append(new_node)
    
    def delete_node(self, del_node):
        """
        Deletes a node from the list of children nodes.

        Parameters:
        - del_node: The node to be deleted.
        """

        self.children = [child for child in self.children if child.board != del_node.board]
    
    def delete_tree(self):
        """
        Deletes all children nodes of the current node.
        """

        self.children = []
    
    def search_node(self, search_node):
        """
        Searches for a specific node in the tree.

        Parameters:
        - search_node: The node to search for.

        Returns:
        - True if the node is found, False otherwise.
        """

        if self.board == search_node.board:
            return True
        return any(child.search_node(search_node) for child in self.children)


pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Tic-Tac-Toe")

board = [[' ' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

def draw_board():
	"""
	Draws the game board on the screen.
	"""

	screen.fill(BG_COLOR)

	# # Load and blit the background image
	# background_image = pygame.image.load('clouds.png')
	# # Zoom out the background image
	# background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
	# screen.blit(background_image, (0, 0))

	# Vertical lines
	for i in range(1, BOARD_COLS):
		pygame.draw.line(screen, LINE_COLOR, (i * (WIDTH // BOARD_COLS), 0), (i * (WIDTH // BOARD_COLS), HEIGHT), LINE_WIDTH)
	# Horizontal lines
	for i in range(1, BOARD_ROWS):
		pygame.draw.line(screen, LINE_COLOR, (0, i * (HEIGHT // BOARD_ROWS)), (WIDTH, i * (HEIGHT // BOARD_ROWS)), LINE_WIDTH)

def draw_figures():
    """
    Draws the X and O figures on the game board.

    """

    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 'X':
                pygame.draw.line(screen, X_COLOR, (col * (WIDTH // BOARD_COLS) + 20, row * (HEIGHT // BOARD_ROWS) + 20), ((col + 1) * (WIDTH // BOARD_COLS) - 20, (row + 1) * (HEIGHT // BOARD_ROWS) - 20), LINE_WIDTH)
                pygame.draw.line(screen, X_COLOR, ((col + 1) * (WIDTH // BOARD_COLS) - 20, row * (HEIGHT // BOARD_ROWS) + 20), (col * (WIDTH // BOARD_COLS) + 20, (row + 1) * (HEIGHT // BOARD_ROWS) - 20), LINE_WIDTH)

            elif board[row][col] == 'O':
                pygame.draw.circle(screen, O_COLOR, (col * (WIDTH // BOARD_COLS) + (WIDTH // BOARD_COLS) // 2, row * (HEIGHT // BOARD_ROWS) + (HEIGHT // BOARD_ROWS) // 2), (min((WIDTH // BOARD_COLS), (HEIGHT // BOARD_ROWS)) // 2) - 20, LINE_WIDTH)

def check_win(board, player):
    """
    Checks if a player has won the game.

    Parameters:
    - board: The current state of the game board.

    - player: The player to check for a win.

    Returns:
    - True if the player has won, False otherwise.
    """

    # Check rows, columns, and diagonals for a win
    for i in range(BOARD_ROWS):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True

    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

def check_draw(board):
    """
    Checks if the game is a draw.

    Parameters:
    - board: The current state of the game board.

    Returns:
    - True if the game is a draw, False otherwise.
    """

    for row in board:
        for cell in row:
            if cell == ' ':
                return False

    return True

def minimax(node):
    """
    Implements the minimax algorithm to determine the best move for
    the AI player.

    Parameters:
    - node: The current node in the minimax tree.

    Returns:

    - The score of the best move.
    """

    if check_win(node.board, 'O'):
        return 1
    elif check_win(node.board, 'X'):
        return -1
    elif check_draw(node.board):
        return 0

    node.generate_children()

    if node.is_maximizing:
        best_score = float("-inf")
        for child in node.children:
            score = minimax(child)
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for child in node.children:
            score = minimax(child)
            best_score = min(score, best_score)
        return best_score

def get_best_move(board, ai_player):
    """
    Determines the best move for the AI player.

    Parameters:
    - board: The current state of the game board.
    - ai_player: The symbol representing the AI player.

    Returns:
    - The coordinates of the best move.
    """

    root = Node(board, 0, ai_player == 'O')
    root.generate_children()

    # Return None if there are no valid moves left
    if not root.children:
        return None

    best_score = float("-inf") if ai_player == 'O' else float("inf")

    best_move = 0 # Initialize to 0 instead of None
    for i, child in enumerate(root.children):
        score = minimax(child)
        if ai_player == 'O' and score > best_score:
            best_score = score
            best_move = i # index of the best move
        elif ai_player == 'X' and score < best_score:
            best_score = score
            best_move = i # index of the best move

    # Introduce a 20% chance of making a random move
    if random.random() < AI_FAIL_RATE and best_move is not None:
        empty_cells = [(i, j) for i in range(BOARD_ROWS) for j in range(BOARD_COLS) if board[i][j] == ' ']
        return random.choice(empty_cells)

    # Find the coordinates of the best move
    for i in range(BOARD_ROWS):
        for j in range(BOARD_COLS):
            if board[i][j] != root.children[best_move].board[i][j]:
                return (i, j)
            

# def display_result_box(message):

#     """
#     Displays the result box with the game outcome.

#     Parameters:
#     - result: The result of the game.
#     """

#     if result == "Draw!":
#         RESULT_BOX_COLOR = (255, 255, 0)  # Yellow for draw
#     elif result == "You Win!":
#         RESULT_BOX_COLOR = (0, 255, 0)  # Green for win
#     else:
#         RESULT_BOX_COLOR = (255, 0, 0)  # Red for lose

#     pygame.draw.rect(screen, RESULT_BOX_COLOR, (100, HEIGHT // 2 - 40, 440, 80))


# def play_result_sound(result):
#     """
#     Plays the appropriate sound based on the game outcome.

#     Parameters:
#     - result: The result of the game.
#     """
#     if result == "Draw!" or result == "You Lose!":
#         lose_or_tie_sound.play()
#     elif result == "You Win!":
#         win_sound.play()


def main():
    # Main game loop
    player_choice = None
    choosing = True
    game_over = False

    player_choice = 'X'

    '''while choosing:
        screen.fill(BG_COLOR)
        draw_choice_buttons()
        pygame.display.update()

        cell_width = WIDTH // BOARD_COLS
        cell_height = HEIGHT // BOARD_ROWS

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = event.pos

            x_button_rect = pygame.Rect(WIDTH // 4 - 75, HEIGHT // 2 - 25, 150, 50)

            o_button_rect = pygame.Rect(WIDTH * 3 // 4 - 75, HEIGHT // 2 - 25, 150, 50)

            if x_button_rect.collidepoint(mouseX, mouseY):
                player_choice = 'X'
                choosing = False
            elif o_button_rect.collidepoint(mouseX, mouseY):
                player_choice = 'O'
                choosing = False
    '''

    # Game setup after player's symbol selection
    if player_choice == 'X':
        player = 'X'
        ai_player = 'O'
    else:
        player = 'O'
        ai_player = 'X'

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and player == player_choice and not game_over:
                mouseX, mouseY = event.pos
                clicked_col = mouseX // (WIDTH // BOARD_COLS)
                clicked_row = mouseY // (HEIGHT // BOARD_ROWS)

                if board[clicked_row][clicked_col] == ' ':
                    board[clicked_row][clicked_col] = player
                    player = ai_player

            if player == ai_player and not game_over:
                best_move = get_best_move(board, ai_player)
                if best_move:
                    row, col = best_move
                    board[row][col] = ai_player
                    player = player_choice

                    # Check game over conditions
                    if check_win(board, player):
                        game_over = True
                    elif check_draw(board):
                        game_over = True

                # Check game over conditions
                if check_win(board, ai_player):
                    game_over = True
                elif check_draw(board):
                    game_over = True

        draw_board()
        draw_figures()

        if rectangle:
            if game_over:
                draw_board()
                draw_figures()

                # result = "Draw!" if check_draw(board) else "You Win!" if check_win(board, player) else "You Lose!"
                # display_result_box(result)

                pygame.display.update()
                pygame.time.wait(2500)
                pygame.quit()
            else:
                pygame.display.update()
        else:
            if game_over:
                draw_board()
                draw_figures()

                result = "Draw!" if check_draw(board) else "You Win!" if check_win(board, player) else "You Lose!"
                # play_result_sound(result)

                pygame.display.update()
                pygame.time.wait(2500)
                pygame.quit()
            else:
                pygame.display.update()

if __name__ == '__main__':
    main()
