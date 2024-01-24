import pygame

class Player(self):
    def __init__(self):
        self.position = [0,0]
        self.speed = 10
        self.size = [50, 50]
        self.health = 5
        self.image = pygame.image.load("images/personaje.png")
        self.up = False
        self.down = False
        self.right = False
        self.left = False

    def movement(self):
        if self.up:
            self.position[1] -= self.speed
        elif self.down:
            self.position[1] += self.speed
        elif self.right:
            self.position[0] += self.speed
        elif self.left:
            self.position[0] -= self.speed


