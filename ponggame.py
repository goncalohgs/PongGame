import pygame, random

# constants for the windows width and height values
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 720

# the RGB values for the colors used in the game
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

def main():

    # GAME SETUP

    # initialize the PyGame library (this is absolutely necessary)
    pygame.init()

    # this creates the window for the game
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # set the window's title
    pygame.display.set_caption("Pong")

    """
    these are the players' game paddles
    the pygame.Rect function need the x, y, width and height
    of the rectangles we will be drawing
    """
    paddle_1_rect = pygame.Rect(30, 0, 7, 100)
    paddle_2_rect = pygame.Rect(SCREEN_WIDTH - 50, 0, 7, 100)

    # this is to track by how much the players' paddles will move per frame
    paddle_1_move = 0
    paddle_2_move = 0

    # this is the rectangle that represents the ball
    ball_rect = pygame.Rect(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 25, 25)

    # determine the x and y speed of the ball (0.1 is just to scale the speed down)
    ball_accel_x = random.randint(2, 4) * 0.1
    ball_accel_y = random.randint(2, 4) * 0.1

    # randomize the direction of the ball
    if random.randint(1, 2) == 1:
        ball_accel_x *= -1
    if random.randint(1, 2) == 1:
        ball_accel_y *= -1

  # GAME LOOP
    while True:
        """
        set the back ground color to black
        needs to be called everytime the game updates
        """
        screen.fill(COLOR_BLACK)

        # checking for events
        for event in pygame.event.get():

        # if the user exits the window
            if event.type == pygame.QUIT:

                # exit the function, to finish the game
                return
            
        # draw player 1 and player 2's paddle rects with the white color
        pygame.draw.rect(screen, COLOR_WHITE, paddle_1_rect)
        pygame.draw.rect(screen, COLOR_WHITE, paddle_2_rect)

        # draw the ball with the white color
        pygame.draw.rect(screen, COLOR_WHITE, ball_rect)

        # update the display (this is necessary for Pygame)
        pygame.display.update()

if __name__ == '__main__':
        main()

