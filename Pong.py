import pygame
import random

# Import the Ball and Paddle classes
import Ball
import Paddle

# Initialize the pygame
pygame.init()
pygame.font.init()

font = pygame.font.SysFont("consolas", 30)

# Set up the game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pong")

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the paddles
paddle_width = 80
paddle_height = 10
paddle_speed = 8
player_paddle_x = WINDOW_WIDTH // 2 - paddle_width // 2
player_paddle_y = WINDOW_HEIGHT - paddle_height - 20

# Set up the ball
ball_radius = 10
ball_speed_x = random.choice([-3, 3])
ball_speed_y = 3
ball_x = WINDOW_WIDTH // 2
ball_y = WINDOW_HEIGHT // 2

# Set up the game clock
clock = pygame.time.Clock()


def main():
    # Game loop
    running = True

    # Create the ball
    ball = Ball.Ball(ball_x, ball_y, ball_radius, ball_speed_x, ball_speed_y)

    # Create the paddles
    player_paddle = Paddle.Paddle(
        player_paddle_x, player_paddle_y, paddle_width, paddle_height, paddle_speed
    )

    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_paddle.get_posx() > 0:
            player_paddle.move_left()
        if (
            keys[pygame.K_RIGHT]
            and player_paddle.get_posx() < WINDOW_WIDTH - paddle_width
        ):
            player_paddle.move_right()

        ball.move()
        ball.check_collision(player_paddle, window)
        score = font.render(f"Score: {ball.get_hit_count()}", True, WHITE)
        window.fill(BLACK)

        player_paddle.display(window)
        ball.display(window)
        window.blit(score, (10, 10))

        # Update the display
        pygame.display.flip()

        # Limit the frame rate
        clock.tick(60)


if __name__ == "__main__":
    main()
    pygame.quit()
