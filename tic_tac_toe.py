import pygame  
import sys

# Initialize pygame
pygame.init()

# Screen settings
size = width, height = 300, 300
line_color = (0, 0, 0)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Tic Tac Toe')

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

# Game board
board = [['' for _ in range(3)] for _ in range(3)]
current_player = 'X'

# Draw grid
def draw_grid():
    screen.fill(white)
    pygame.draw.line(screen, line_color, (100, 0), (100, 300), 3)
    pygame.draw.line(screen, line_color, (200, 0), (200, 300), 3)
    pygame.draw.line(screen, line_color, (0, 100), (300, 100), 3)
    pygame.draw.line(screen, line_color, (0, 200), (300, 200), 3)

# Draw X and O
def draw_marks():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 'X':
                pygame.draw.line(screen, red, (col * 100 + 20, row * 100 + 20), (col * 100 + 80, row * 100 + 80), 5)
                pygame.draw.line(screen, red, (col * 100 + 80, row * 100 + 20), (col * 100 + 20, row * 100 + 80), 5)
            elif board[row][col] == 'O':
                pygame.draw.circle(screen, blue, (col * 100 + 50, row * 100 + 50), 40, 5)

# Check for win
def check_winner(player):
    for row in board:
        if row.count(player) == 3:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

# Main game loop
def game_loop():
    global current_player
    game_over = False
    draw_grid()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                x, y = event.pos
                row, col = y // 100, x // 100
                if board[row][col] == '':
                    board[row][col] = current_player
                    if check_winner(current_player):
                        game_over = True
                    current_player = 'O' if current_player == 'X' else 'X'
                    draw_grid()
                    draw_marks()

        pygame.display.update()

game_loop()
