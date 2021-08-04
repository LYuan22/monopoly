import pygame
import random

class Roll: # Every side of the dice is its own object, of this class.
    def __init__(self, image, value):
        self.image = image
        self.value = value

def rollDice(die):
    roll1 = random.choice(die)
    roll2 = random.choice(die)
    return [roll1, roll2]

dieOne = Roll(pygame.image.load('images/dice/one.png'), 1)
dieTwo = Roll(pygame.image.load('images/dice/two.png'), 2)
dieThree = Roll(pygame.image.load('images/dice/three.png'), 3)
dieFour = Roll(pygame.image.load('images/dice/four.png'), 4)
dieFive = Roll(pygame.image.load('images/dice/five.png'), 5)
dieSix = Roll(pygame.image.load('images/dice/six.png'), 6)

die = [dieOne, dieTwo, dieThree, dieFour, dieFive, dieSix]

roll = 0
throw = [0, 0]
