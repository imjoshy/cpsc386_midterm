import pygame as pg
from pygame.sprite import Sprite, Group     # for lasers


# Included just to remove red lines in Ship's fire method
class Laser(Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        # . . . -- rest of implementation


""" (25 pts) Write the code or pseudo-code in Python for the Ship class """


class Ship:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.speed = 2      # speed of 2 used for X and Y directions
        self.image = pg.image.load('ship_image_here')       # CHANGE parameter to name of ship image in file
        self.rect = self.image.get_rect()

        self.x = 0
        self.y = 0

        # These ASSUME that the Game class has a WIDTH and HEIGHT for the screen
        self.rect.centerx = self.game.WIDTH / 2     # X starts in the center of the screen
        self.rect.centery = self.game.HEIGHT * (2/3)        # Just go 2/3 down the screen

        self.lasers = Group()

    # center the ship (reset to starting position
    def center_ship(self):
        self.rect.centerx = self.game.WIDTH / 2
        self.rect.centery = self.game.HEIGHT * (2/3)

    # create a laser and add it to the Group
    def fire(self):
        laser = Laser(game=self.game)
        self.lasers.add(laser)

    def remove_lasers(self):
        self.lasers.remove()        # remove the lasers (Group)

    def move(self):
        # self.x and self.y should change *IN Game CLASS* depending on user input (W, A, S, D)
        # W -- should set self.y to 1 // S -- set self.y to -1 // A -- set self.x to -1 // D set self.x to 1
        self.rect.centerx += self.x + self.speed
        self.rect.centery += self.y + self.speed

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.move()
        self.draw()


""" (25 pts) Write the code or pseudo-code in Python for the Vector class """


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector ({}, {})'.format(self.x, self.y)

    def __add__(self, other):       # other is another vector
        x = self.x + other.x
        y = self.y + other.y

        return Vector(x, y)     # return new vector

    def __sub__(self, other):       # other is another vector
        x = self.x - other.x
        y = self.y - other.y

        return Vector(x, y)

    def __rmul__(self, k: float):       # Vector() * k
        x = self.x * k
        y = self.y * k

        return Vector(x, y)     # return new vector

    def __mul__(self, k: float):        # k * Vector()
        return self * k     # should work because rmul overloaded above

    def __truediv__(self, k: float):
        x = self.x / k
        y = self.y / k

        return Vector(x, y)     # return new vector

    def __neg__(self):
        self.x *= -1
        self.y *= -1
        # note! changing current vector, not making a new one

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y      # return bool result

    @staticmethod
    def test():
        v = Vector(x=5, y=5)
        u = Vector(x=4, y=4)

        print('v is {}'.format(v))
        print('u is {}'.format(u))

        print('u + v is {}'.format(u + v))
        print('u - v is {}'.format(u - v))

        print('3 * u is {}'.format(3 * u))

        print('-u is {}'.format(-1 * u))


def main():
    Vector.test()


if __name__ == '__main__':
    main()
