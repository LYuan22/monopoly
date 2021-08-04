import pygame

housePic = pygame.image.load('images/house.png')
hotelPic = pygame.image.load('images/hotel.png')
houseSidePic = pygame.image.load('images/houseSide.png')
hotelSidePic = pygame.image.load('images/hotelSide.png')

buildingPics = [
    housePic, hotelPic,
    houseSidePic, hotelSidePic,
    pygame.transform.rotate(housePic, 180), pygame.transform.rotate(hotelPic, 180),
    pygame.transform.rotate(houseSidePic, 180), pygame.transform.rotate(hotelSidePic, 180),
]

# Rent you pay at each house level for each street
houseCostGrid = [
    [
        [2, 10, 30, 90, 160, 250], [4, 20, 60, 180, 320, 450]
    ], [
        [6, 30, 90, 270, 400, 550], [8, 40, 100, 300, 450, 600]
    ], [
        [10, 50, 150, 450, 625, 750], [12, 60, 180, 500, 700, 900]
    ], [
        [14, 70, 200, 550, 750, 950], [16, 80, 220, 600, 800, 1000]
    ], [
        [18, 90, 250, 700, 875, 1050], [20, 100, 300, 750, 925, 1100]
    ], [
        [22, 110, 330, 800, 975, 1150], [24, 120, 360, 850, 1025, 1200]
    ], [
        [26, 130, 390, 900, 1100, 1275], [28, 150, 450, 1000, 1200, 1400]
    ], [
        [35, 175, 500, 1100, 1300, 1500], [50, 200, 600, 1400, 1700, 2000]
    ]
]

mortgagePic = pygame.image.load('images/mortgage.png')
mortgagePic2 = pygame.transform.rotate(mortgagePic, 90)