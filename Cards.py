import pygame
import random

class Card: # Chance and Community Chest cards
    def __init__(self, text, type, value):
        self.text = text
        self.type = type
        self.value = value
        self.executed = False

    def execute(self, player): # A set of conditionals that do different stuff to the player who picked the card.
        if self.type == 'pay':
            player.money += self.value
        elif self.type == 'move':
            if player.boardpos > self.value:
                player.money += 200
            player.boardpos = self.value
        elif self.type == 'go to jail':
            player.inJail = True
        elif self.type == 'gojf':
            if self.text.__contains__('bribed'):
                player.getOutOfJailFreeCards.append(communityChest[4])
            else:
                player.getOutOfJailFreeCards.append(chance[8])
            player.canRoll = False
        elif self.type == 'social':
            for sprite in players:
                if sprite == player:
                    sprite.money += self.value*(len(players)-1)
                else:
                    sprite.money -= self.value
        elif self.type == 'repairs':
            for prop in properties:
                if prop.owner == player:
                    if prop.houses > 4:
                        player.money -= self.value[1]
                    else:
                        player.money -= self.value[0]*prop.houses
        elif self.type == 'nearestu':
            if 0 < player.boardpos <= 12:
                player.boardpos = 12
            elif 28 < player.boardpos < 40:
                player.boardpos = 12
                player.money += 200
            else:
                player.boardpos = 28
        elif self.type == 'nearests':
            if 0 < player.boardpos <= 5:
                player.boardpos = 5
            elif player.boardpos <= 15:
                player.boardpos = 15
            elif player.boardpos <= 25:
                player.boardpos = 25
            elif player.boardpos <= 35:
                player.boardpos = 35
            else:
                player.boardpos = 5
                player.money += 200
        elif self.type == 'mover':
            player.boardpos += self.value


class Chance: # There ultimately wasn't much point in writing this class except to help identify squares by their type.
    def __init__(self, name, boardpos):
        self.name = name
        self.boardpos = boardpos
        if self.name == 'Chance':
            self.list = chance
        else:
            self.list = communityChest

    def pickCard(self):
        return random.choice(self.list)

gojfCC = pygame.image.load('images/gojfComChest.png')
gojfC = pygame.image.load('images/gojfChance.png')

communityChest = [
    Card('Advance to Go. Collect $400.', 'move', 0), Card("The bank's web server got #COVID and accidentally deposits #into your account. Collect $200.", 'pay', 200),
    Card("You hurt yourself but there's #no socialised medicine. #Pay $50 and remember- you have #nothing to lose but your chains.", 'pay', -50),
    Card('You made some banger #investments. Collect $50.', 'pay', 50), Card('You argue that you murdered #the child in self defence: #Get out of Jail free.', 'gojf', gojfCC),
    Card('The government planted drugs #on you to meet prison quotas. #Go to Jail. Go directly to Jail. #Do not pass Go, do not collect $200.', 'go to jail', 0),
    Card('Your great-Aunt Gertrude #kicks the bucket. Inherit $100', 'pay', 100),
    Card('Happy Birthday! #Collect $10 from every player', 'social', 10), Card('You and your life insurance mature. #Collect $100', 'pay', 100),
    Card("You got COVID- pay #hospital fees of $50", 'pay', -50), Card('Your friend Banquo was #prophecised to father #a line of kings. #Pay $50 to hire a hitman', 'pay', -50),
    Card('You find $25 bucks on the #ground. Its your lucky day.', 'pay', 25), Card('Make hardcore repairs #on all your property. #For each house pay $40, #for each hotel pay $115', 'repairs', [40, 115]),
    Card('You have come last in a #beauty contest. Collect $10 #sympathy money', 'pay', 10), Card('Your co-worker gives you $100 #not to tell anyone about his #heroin addiction', 'pay', 100)
]
chance = [
    Card('Advance to Go. Collect $400.', 'move', 0), Card('Advance to Russia. #If you pass Go, collect $200.', 'move', 24), Card('Advance to China. #If you pass Go, collect $200.', 'move', 39),
    Card('Advance to Congo. #If you pass Go, collect $200.', 'move', 11), Card('Advance to North Station. #If you pass Go, collect $200.', 'move', 5),
    Card('Advance to the nearest utility. #If you pass Go, collect $200', 'nearestu', 0),
    Card('Advance to the nearest station. #If you pass Go, collect $200', 'nearests', 0),
    Card('Bank pays you some of that #sweet sweet mullah. Collect $50.', 'pay', 50), Card('You bribe the cops with donuts: #Get out of jail free', 'gojf', gojfC), Card('Go back 3 spaces', 'mover', -3),
    Card('You infringed the copyright of #a popular board game. #Go to Jail. Go directly to Jail. #Do not pass Go, do not collect $200.', 'go to jail', 0),
    Card('Make general repairs on all your #property. For each house pay $25, #for each hotel pay $100', 'repairs', [25, 100]), Card('25 bucks fall out of your pocket. #You lament the lack of women\'s #shorts with reasonably-sized pockets', 'pay', -25),
    Card("You have mysteriously #become everybody's grandma. #Pay each player #$50 as a present.", 'social', -50), Card('Your investment in divorce #lawyers was successful. #Collect $150.', 'pay', 150)
]

