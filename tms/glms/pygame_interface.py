import pygame
import pygame_menu
import requests

pygame.init()

# Load and scale the character image
character_image = pygame.image.load('assets/images/lang.png')
character_image = pygame.transform.scale(character_image, (230, 230))
bg_image = pygame.image.load('assets/images/intro_scene.png')

# Set the velocity for character movement
velocity = 3
obstacle = pygame.Rect(300, 500, 250, 60)

# Set initial coordinates for the character
x_position = 225
y_position = 100
object_x_position = 225
object_y_position = 50

# Set up display
surface = pygame.display.set_mode((object_x_position, object_y_position))
window_width, window_height = 800, 600
screen = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()
pygame.display.set_caption('GLMS_01')

# Set up font
font = pygame.font.Font(None, 36)

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# API URL
API_URL = "http://localhost:8000/studentsApi/"

def fetch_student_data():
    """Fetch student data from the API."""
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

def display_text(text, x, y):
    """Render text on the screen at a specified position."""
    text_surface = font.render(text, True, BLACK)
    screen.blit(text_surface, (x, y))

def main():
    """Main function to run the Pygame application."""
    global x_position, y_position

    running = True
    student_data = fetch_student_data()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Get the set of keys currently being pressed
        keys = pygame.key.get_pressed()

        # Update character's position based on key presses
        if keys[pygame.K_LEFT] and x_position > 0:
            x_position -= velocity
        if keys[pygame.K_RIGHT] and x_position < window_width - character_image.get_width():
            x_position += velocity
        if keys[pygame.K_UP] and y_position > 0:
            y_position -= velocity
        if keys[pygame.K_DOWN] and y_position < window_height - character_image.get_height():
            y_position += velocity

        # Create a smaller Rect for the character
        collision_rect = pygame.Rect(
            x_position + 10,
            y_position - 20,
            character_image.get_width() - 10,
            character_image.get_height() - 0
        )

        # Fill the screen with white
        screen.fill(WHITE)

        # Display student data (if needed)
        y_offset = 50
        for student in student_data:
            student_info = f"Username: {student.get('username', 'N/A')}"
            display_text(student_info, 50, y_offset)
            y_offset += 50

        # Draw the background
        screen.blit(bg_image, (0, 0))

        # Draw the character
        screen.blit(character_image, (x_position, y_position))

        # Draw the obstacle
        pygame.draw.rect(screen, (0, 0, 0), obstacle, 4)

        # Check for collision with the obstacle
        if collision_rect.colliderect(obstacle):
            pygame.draw.rect(screen, BLACK, obstacle)
            display_text("Collision detected!", 500, 300)

        # Update the display
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

def start_game():
    """Function to start the game from the menu."""
    main()

def create_menu():
    menu = pygame_menu.Menu('Introduction', 400, 300,
                            theme=pygame_menu.themes.THEME_BLUE)
    menu.add.button('Play', start_game)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(screen)

if __name__ == "__main__":
    create_menu()

