import pygame, random

konto = 1000000

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 400, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Slot Machine")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Load fruit images
SYMBOLS = ['ananas', 'apple', 'cherry', 'grape', 'strawberry']
images = {symbol: pygame.image.load(f"{symbol}.png") for symbol in SYMBOLS}

PAYOUTS = {
    ('ananas', 'ananas', 'ananas'): 5,
    ('apple', 'apple', 'apple'): 10,
    ('cherry', 'cherry', 'cherry'): 20,
    ('grape', 'grape', 'grape'): 50,
    ('strawberry', 'strawberry', 'strawberry'): 100,  # Jackpot
}

# Font
font = pygame.font.Font(None, 50)
button_font = pygame.font.Font(None, 30)

# Game variables
bet = 5
slots = [random.choice(SYMBOLS) for _ in range(3)]

# Button positions
spin_button = pygame.Rect(150, 400, 100, 50)
increase_bet_button = pygame.Rect(270, 400, 50, 50)
decrease_bet_button = pygame.Rect(80, 400, 50, 50)

# Function to draw the slot machine
def draw_machine():
    global konto
    screen.fill(WHITE)
    balance_text = font.render(f"Balance: ${konto}", True, BLACK)
    bet_text = font.render(f"Bet: ${bet}", True, BLACK)
    screen.blit(balance_text, (10, 10))
    screen.blit(bet_text, (10, 50))
    global slots
    for i, symbol in enumerate(slots):
        screen.blit(images[symbol], (80 + i * 100, 150))
    
    # Draw buttons
    pygame.draw.rect(screen, BLUE, spin_button)
    pygame.draw.rect(screen, GRAY, increase_bet_button)
    pygame.draw.rect(screen, GRAY, decrease_bet_button)
    
    spin_text = button_font.render("Spin", True, WHITE)
    plus_text = button_font.render("+", True, BLACK)
    minus_text = button_font.render("-", True, BLACK)
    
    screen.blit(spin_text, (spin_button.x + 25, spin_button.y + 10))
    screen.blit(plus_text, (increase_bet_button.x + 15, increase_bet_button.y + 10))
    screen.blit(minus_text, (decrease_bet_button.x + 15, decrease_bet_button.y + 10))
    
    pygame.display.flip()

# Function for spinning animation
def spin_animation():
    global slots
    initial_slots = slots.copy()
    for _ in range(10):
        slots = [random.choice(SYMBOLS) for _ in range(3)]
        draw_machine()
        pygame.display.flip()
        pygame.time.delay(100)
    slots = initial_slots


# Function to spin
def spin():
    global konto
    if konto < bet:
        return
    konto -= bet
    spin_animation()
    draw_machine()
    check_win()

# Function to check for winnings
def check_win():
    global konto
    if tuple(slots) in PAYOUTS:
        winnings = bet * PAYOUTS[tuple(slots)]
        konto += winnings
        highlight_win()
        pygame.time.delay(500)

# Function to highlight winnings
def highlight_win():
    pygame.draw.rect(screen, GREEN, (70, 140, 260, 100), 5)
    pygame.display.flip()
    pygame.time.delay(500)

# Main loop
running = True
while running:
    draw_machine()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if spin_button.collidepoint(event.pos):
                spin()
            elif increase_bet_button.collidepoint(event.pos) and bet < konto:
                bet += 5
            elif decrease_bet_button.collidepoint(event.pos) and bet > 5:
                bet -= 5

pygame.quit()