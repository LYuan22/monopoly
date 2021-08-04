import pygame
import math
import random
import time
from pygame import mixer

boot = pygame.image.load('images/pieces/boot.png')
car = pygame.image.load('images/pieces/car.png')
dog = pygame.image.load('images/pieces/dog.png')
hat = pygame.image.load('images/pieces/hat.png')
iron = pygame.image.load('images/pieces/iron.png')
ship = pygame.image.load('images/pieces/ship.png')
thimble = pygame.image.load('images/pieces/thimble.png')
wheelbarrow = pygame.image.load('images/pieces/wheelbarrow.png')

pieces = [boot, car, dog, hat, iron, ship, thimble, wheelbarrow]

class Player: # Class for practical matters considering the user and Eve.
    def __init__(self, name, isTurn, screens):
        self.name = name
        self.piece = None
        self.boardpos = 0
        self.timeMoving = 0
        self.pieceSelected = False
        self.pieceConfirmed = False
        self.colour = None
        self.isTurn = isTurn
        self.money = 1500
        self.screens = screens #
        self.canRoll = True
        self.doublesCount = 0
        self.inJail = False
        self.jailTurns = 0
        self.getOutOfJailFreeCards = []
        # The next 4 attributes are boolean statuses (statuses? statii?). Arguably I could have made one string attribute called 'status'. Ah, the joy of hindsight.
        self.isDeveloping = False
        self.isTrading = False
        self.isMortgaging = False
        self.normalGameplay = True
        self.offer = []
        self.bid = '0'
        self.firstTimeInJail = True
        self.paidOOJ = False #OOJ stands for Out Of Jail. It gets tedious to write.


    def choosePiece(self, mousepos): # Lets the user choose a piece.
        if 110 < mousepos[0] < 110 + 1*270:
            if 276 < mousepos[1] < 276 + 128:
                self.piece = boot
                return (110, 276)
            elif 427 < mousepos[1] < 427 + 128:
                self.piece = iron
                return (110, 427)
        elif 110 + 1*270 < mousepos[0] < 110 + 2*270:
            if 276 < mousepos[1] < 276 + 128:
                self.piece = car
                return (110 + 1*270, 276)
            elif 427 < mousepos[1] < 427 + 128:
                self.piece = ship
                return (110 + 1 * 270, 427)
        elif 110 + 2*270 < mousepos[0] < 110 + 3*270:
            if 276 < mousepos[1] < 276 + 128:
                self.piece = dog
                return (110 + 2 * 270, 276)
            elif 427 < mousepos[1] < 427 + 128:
                self.piece = thimble
                return (110 + 2 * 270, 427)
        elif 110 + 3*270 < mousepos[0] < 110 + 4*270:
            if 276 < mousepos[1] < 276 + 128:
                self.piece = hat
                return (110 + 3 * 270, 276)
            elif 427 < mousepos[1] < 427 + 128:
                self.piece = wheelbarrow
                return (110 + 3 * 270, 427)
        else:
            return False

    def getPos(self): # 'Boardpos' is an integer from 0-39 depending on what square you're on, but that has to be translated into x and y co-ords, hence this function.
        if 0 <= self.boardpos < 10:
            return [608-57*self.boardpos, 630]
        elif 10 <= self.boardpos < 20:
            return [15, 608-57*(self.boardpos-10)]
        elif 20 <= self.boardpos < 30:
            return [38 + 57*(self.boardpos-20), 15]
        else:
            return [630, 38 + 57*(self.boardpos-30)]

    def move(self): # Moves players forward one place at a time. I'm pretty sure it gets called on every iteration of the loop.
        if self.timeMoving > 0:
            if self.boardpos == 39:
                self.boardpos = 0
                self.money += 200
            else:
                self.boardpos += 1
            time.sleep(0.1)
            self.timeMoving -= 1