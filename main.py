import pygame
import random
import math

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (230, 70, 30)

ScreenY = 720
ScreenX = 1280

Ball_S = 10
Friction = 0.00

class Ball:
    def __init__(self):
        # pos and vel
        self.x = 0
        self.y = 0
        self.change_x = 0
        self.change_y = 0

        # type and color
        self.color = WHITE

def make_ball():
    ball = Ball()
    # Starting position of the ball.
    ball.x = random.randrange(Ball_S, ScreenX - Ball_S)
    ball.y = random.randrange(Ball_S, ScreenY - Ball_S)
 
    # Speed and direction of ball
    ball.change_x = random.randrange(-5, 5)
    ball.change_y = random.randrange(-5, 5)
 
    return ball

def move(c, v, r, m):
    c += v
    if c < r:
        c, v = r, -v
    if c > m-r:
        c, v = m - r, -v   
    return c, v

def main():
    pygame.init()

    screen = pygame.display.set_mode([ScreenX, ScreenY])
    pygame.display.set_caption("Friction")

    ball_list = []

    for x in range(30):
        ball = make_ball()
        ball_list.append(ball)

    clock = pygame.time.Clock()

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # --- Logic
        for ball in ball_list:

            ball.x, ball.change_x = move(ball.x, ball.change_x, Ball_S, ScreenX)
            ball.y, ball.change_y = move(ball.y, ball.change_y, Ball_S, ScreenY)

            for a in ball_list:
                if a != ball:
                    v1 = pygame.math.Vector2(ball.x, ball.y)
                    v2 = pygame.math.Vector2(a.x, a.y)

                    if v1.distance_to(v2) < Ball_S + Ball_S:
                        ball.color = RED
                        a.color = RED

                        nv = v2 - v1

                        m1 = pygame.math.Vector2(ball.change_x, ball.change_y).reflect(nv)
                        m2 = pygame.math.Vector2(a.change_x, a.change_y).reflect(nv)

                        if m1.y < 0:
                            m1.y += Friction * 10
                        if m1.y > 0:
                            m1.y -= Friction * 10

                        if m1.x < 0:
                            m1.x += Friction * 10
                        if m1.x > 0:
                            m1.x -= Friction * 10
                        if m2.y < 0:
                            m2.y += Friction * 10
                        if m2.y > 0:
                            m2.y -= Friction * 10

                        if m2.x < 0:
                            m2.x += Friction * 10
                        if m2.x > 0:
                            m2.x -= Friction * 10

                        ball.change_x, ball.change_y = m1.x, m1.y
                        a.change_x, a.change_y = m2.x, m2.y
                    
                    else:
                        ball.color = WHITE

            if ball.change_y < 0:
                ball.change_y += Friction
            if ball.change_y > 0:
                ball.change_y -= Friction

            if ball.change_x < 0:
                ball.change_x += Friction
            if ball.change_x > 0:
                ball.change_x -= Friction

            if ball.change_y < 0.01 and ball.change_y > -0.01:
                ball.change_y = 0
            if ball.change_x < 0.01 and ball.change_x > -0.01:
                ball.change_x = 0

        screen.fill(BLACK)
 
        # Draw the balls
        for ball in ball_list:
            pygame.draw.circle(screen, ball.color, [ball.x, ball.y], Ball_S)
 
        clock.tick(60)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()