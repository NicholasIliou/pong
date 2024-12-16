from __future__ import annotations
import pygame

class Rect:
    def __init__(self, screen:pygame.Surface, y_pos: int, x_pos: int, width: int, height: int, color:list[int] | str ="white"):
        """
        Initialize a Bar object.
        :param y_pos: The y-coordinate position of the bar.
        :param x_pos: The x-coordinate position of the bar.
        :param width: The width of the bar.
        :param height: The height of the bar.
        """

        self.screen = screen
        self.y_pos = y_pos
        self.x_pos = x_pos
        self.width = width
        self.height = height
        self.color = color
    
    def collisions(self):
        lst=[]
        for x in range(int(self.y_pos),int(self.y_pos)+int(self.height)):
            lst.append(x)
        return lst

    def draw(self):
        pygame.draw.rect(
            self.screen,
            self.color,
            (self.x_pos,
            self.y_pos,
            self.width,
            self.height)
        )

class Point:
    def __init__(self,y:int,x:int):
        self.y=y
        self.x=x

    def center_align(self, screen: pygame.Surface)->Point:
        self.y = screen.get_width() / 2
        self.x = screen.get_height() / 2

class Circle:
    def __init__(self, center:Point,screen:pygame.Surface, radius:int, color:list[int] | str ="white"):
        self.screen = screen
        self.color = color
        self.center = center
        self.radius = radius

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.center.x,
            self.center.y),
            self.radius
        )

class Ball:
    def __init__(
            self,
            circle:Circle,
            screen: pygame.Surface,
            x_velocity:int = 1,
            y_velocity:int =1
            ): 
        
        self.screen = screen
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity
        self.ball = circle
    
    def update_velocity(self,rectangle_left:Rect,rectangle_right:Rect):
        """Check for collisions and reverse velocity"""
        if self.ball.center.x <= rectangle_left.x_pos:
            if self.ball.center.y in rectangle_left.collisions():
                self.x_velocity *= -1

        if self.ball.center.x >= rectangle_right.x_pos:
            if self.ball.center.y in rectangle_right.collisions():
                self.x_velocity *= -1

        if self.ball.center.y <= 0 or self.ball.center.y >= self.screen.get_height():
            self.y_velocity *= -1

    def reset(self,screen:pygame.Surface):
        if self.ball.center.x <= 0 or self.ball.center.x >= self.screen.get_width():
            self.ball.center.x = screen.get_width() / 2
            self.ball.center.y = screen.get_height() / 2
    
    def move(self,rect_left:Rect, rect_right:Rect):
        """
        moves the ball depending on the velocity of the object.
        execute in loop for animation
        """
        self.update_velocity(rect_left,rect_right)
        self.ball.center.x += self.x_velocity
        self.ball.center.y += self.y_velocity