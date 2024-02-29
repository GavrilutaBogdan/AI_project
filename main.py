import pygame
import sys
import numpy as np
from kalah import Kalah
# Initialize Pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Kalaha")

# Define colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Define constants for the board
PIT_RADIUS = 30
PIT_DISTANCE = 80
KALAHA_WIDTH = 100
KALAHA_HEIGHT = 250
PLAYER1_PITS = [(200 + i * PIT_DISTANCE, 100) for i in range(6)]
PLAYER2_PITS = [(200 + i * PIT_DISTANCE, 300) for i in range(6)]
PLAYER1_KALAHA = (50, 75)
PLAYER2_KALAHA = (650, 75)

# Number of stones in each pit
PLAYER1_STONES = [4, 4, 4, 4, 4, 4]
PLAYER2_STONES = [4, 4, 4, 4, 4, 4]
# Number of stones in each KALAHA
KALAHA_STONES_PLAYER1 = 0
KALAHA_STONES_PLAYER2 = 0
# Initialize Pygame font
pygame.font.init()
font = pygame.font.SysFont(None, 36)

# Variable to track current player's turn
current_player = 1  # Player 1 starts

# Draw the game board
def draw_board():
    screen.fill(WHITE)
    # Draw player 1 pits and stones
    for i, (pit_position, stones) in enumerate(zip(PLAYER1_PITS, PLAYER1_STONES)):
        draw_pit(pit_position, BLUE, stones)
    # Draw player 2 pits and stones
    for i, (pit_position, stones) in enumerate(zip(PLAYER2_PITS, PLAYER2_STONES)):
        draw_pit(pit_position, RED, stones)
    # Draw player 1 Kalaha
    draw_kalaha(PLAYER1_KALAHA, BLUE,KALAHA_STONES_PLAYER1)
    # Draw player 2 Kalaha
    draw_kalaha(PLAYER2_KALAHA, RED,KALAHA_STONES_PLAYER2)

    # Display whose turn it is
    if current_player == 1:
        text_surface = font.render("Player 1's Turn", True, BLACK)
    else:
        text_surface = font.render("Player 2's Turn", True, BLACK)
    text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, 50))
    screen.blit(text_surface, text_rect)

    pygame.display.flip()

def draw_pit(position, color, stones):
    pygame.draw.circle(screen, color, position, PIT_RADIUS)
    text_surface = font.render(str(stones), True, BLACK)  # Render stones in black color
    text_rect = text_surface.get_rect(center=position)
    screen.blit(text_surface, text_rect)

def draw_kalaha(position, color,kalaha_stones):
    pygame.draw.rect(screen, color, pygame.Rect(position[0], position[1], KALAHA_WIDTH, KALAHA_HEIGHT))
    text_surface = font.render(str(kalaha_stones), True, BLACK)
    text_rect = text_surface.get_rect(center=(position[0] + KALAHA_WIDTH // 2, position[1] + KALAHA_HEIGHT // 2))
    screen.blit(text_surface, text_rect)
        

# Function to check for a winner
def check_winner():
    if sum(PLAYER1_STONES) == 0:
        print("Player 2 wins!")
        return True
    elif sum(PLAYER2_STONES) == 0:
        print("Player 1 wins!")
        return True
    return False

# Function to handle keyboard input
def handle_key(key):
    global current_player
    game = Kalah()
    state = 0
    # Check if it's a valid key for the current player
    if current_player == 1:
        if pygame.K_1 <= key <= pygame.K_6:
            pit_index = key - pygame.K_1
            
            game.move(pit_index)  # Player 1's turn
            KALAHA_STONES_PLAYER1 = game.table[0]
            KALAHA_STONES_PLAYER1 = game.table[1]
            PLAYER1_STONES = game.dep[0]
            PLAYER2_STONES = game.dep[1]
            current_player = 1  # Switch to Player 2's turn
    elif current_player == 2:
            if key == pygame.K_q:
                pit_index = 0
                state =1
                current_player = 2  # Switch to Player 1's turn
            elif key == pygame.K_w: 
                pit_index = 1
                state =1
                current_player = 2  # Switch to Player 1's turn
            elif key == pygame.K_e:
                pit_index = 2
                state =1
                current_player = 2  # Switch to Player 1's turn
            elif key == pygame.K_r:
                pit_index = 3
                state =1
                current_player = 2  # Switch to Player 1's turn
            elif key == pygame.K_t:
                pit_index = 4
                state =1
                current_player = 2  # Switch to Player 1's turn
            elif key == pygame.K_y:
                pit_index = 5
                state =1 
                current_player = 2  # Switch to Player 1's turn
            if state ==1 :
                game.move(pit_index)  # Player 1's turn
                KALAHA_STONES_PLAYER1 = game.table[0]
                KALAHA_STONES_PLAYER1 = game.table[1]
                PLAYER1_STONES = game.dep[0]
                PLAYER2_STONES = game.dep[1]

                

# Draw the initial game board
draw_board()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            handle_key(event.key)
            draw_board()
            if check_winner():
                #running = False
                print("game over")

# Quit Pygame
pygame.quit()
sys.exit()
