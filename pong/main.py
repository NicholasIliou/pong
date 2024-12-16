from __future__ import annotations
import pygame
from objects import *
        
if __name__ == "__main__":

    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    dt = 0
    center = Point(1,1)
    center.center_align(screen)
    ball = Ball(Circle(center, screen, 10),screen,x_velocity=3,y_velocity=3)
    bar_left = Rect(screen,10,10,10,100,"white")
    bar_right = Rect(screen,10,screen.get_width()-20,10,100,"white")
    paddle_speed = 3

    # Quit Game
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")

        # Game
        ball.ball.draw()
        ball.move(bar_left,bar_right)
        ball.reset(screen)

        # draw bars
        bar_left.draw()
        bar_right.draw()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            bar_left.y_pos -= paddle_speed
        if keys[pygame.K_s]:
            bar_left.y_pos += paddle_speed
        if keys[pygame.K_UP]:
            bar_right.y_pos -= paddle_speed
        if keys[pygame.K_DOWN]:
            bar_right.y_pos += paddle_speed

        # flip display & clock
        pygame.display.flip()
        dt = clock.tick(280) / 1000

    pygame.quit
    