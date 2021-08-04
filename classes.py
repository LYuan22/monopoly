import pygame

class Palette: # Aside from the house colours, there are only six colours that I use in the game, ranging from darkish green to yellowish brown. I found the palette online, hence the fancy colour names.
    def __init__(self):
        self.axolotl = (115, 128, 84)
        self.olivine = (163, 168, 109)
        self.dutchWhite = (225, 213, 184)
        self.darkVanilla = (214, 199, 167)
        self.camel = (190, 153, 110)
        self.darkGold = (170, 114, 42)


class MoneyOffer: # Used in trades
    def __init__(self, value):
        self.value = value
        self.name = '$' + str(self.value)
        self.colour = value

class Ratio: # Part of Eve's property valuing system
    def __init__(self, cost, rent):
        self.cost = cost
        self.rent = rent
        self.value = self.cost/self.rent

class Bank: # An identifier class. It is reminiscent of real life banks though.
    def __init__(self):
        self.colour = None

class Button: # The menu is made up of buttons, which are in the list 'buttons' and belong to this class.
    def __init__(self, pos, size):
        self.pos = pos
        self.size = size
        self.left = pos[0]
        self.top = pos[1]
        self.right = pos[0] + size[0]
        self.bottom = pos[1] + size[1]
        self.middle = ((self.left+self.right)//2, (self.top+self.bottom)//2)
    def mouseHover(self): # Returns True if the mouse is over the button.
        mousepos = pygame.mouse.get_pos()
        if self.left < mousepos[0] < self.right and self.top < mousepos[1] < self.bottom:
            return True
        return False

