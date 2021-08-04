import pygame

# Here are the screens for the animations when someone wins. I'm not sure how to actually do gifs so I draw different pictures every 0.2 seconds.
ugos1 = pygame.image.load('images/game over/user1.png')
ugos2 = pygame.image.load('images/game over/user2.png')
ugos3 = pygame.image.load('images/game over/user3.png')
ugos4 = pygame.image.load('images/game over/user4.png')
ugos5 = pygame.image.load('images/game over/user5.png')

ugoScreens = [ugos1, ugos2, ugos3, ugos4, ugos5]

cgos1 = pygame.image.load('images/game over/CPU1.png')
cgos2 = pygame.image.load('images/game over/CPU2.png')
cgos3 = pygame.image.load('images/game over/CPU3.png')

cgoScreens = [cgos1, cgos2, cgos3]



winner = None

# -------------------------------------------------------------------------------
# BOARD
board = pygame.image.load("images/board.png")

squares = []
properties = []
streets = [[],[],[],[],[],[],[],[]]

# -------------------------------------------------------------------------------
# AI SETUP

costRatios = []
houseRatios = []
rejectedTrades = []

# -------------------------------------------------------------------------------
# COLOURS
colours = ['red', 'orange', 'yellow', 'green', 'teal', 'blue', 'indigo', 'purple', 'station', 'utility', 'undefined']

axolotlPiece = pygame.image.load('images/pieces/axolotlPiece.png')
darkVanillaPiece = pygame.image.load('images/pieces/darkVanillaPiece.png')
camelPiece = pygame.image.load('images/pieces/camelPiece.png')
darkGoldPiece = pygame.image.load('images/pieces/darkGoldPiece.png')

pieceColours = [axolotlPiece, camelPiece, darkGoldPiece]


#Alerts
choiceAlertPic = pygame.image.load('images/choiceAlert.png')
alertPic = pygame.image.load('images/alert.png')
confirmAlertPic = pygame.image.load('images/confirmAlert.png')
tradeAlertPic = pygame.image.load('images/tradeAlert.png')