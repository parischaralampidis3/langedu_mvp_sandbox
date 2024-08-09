import pygame
import requests

pygame.init()

# Set up display
window_width, window_height = 800, 600
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('GLMS_01')

# Set up font
font = pygame.font.Font(None, 36)

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

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
    running = True
    student_data = fetch_student_data()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)

        y_offset = 50
        for student in student_data:
            student_info = f"Username: {student.get('username', 'N/A')}"
            display_text(student_info, 50, y_offset)
            y_offset += 50

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
