class Alert:
    def __init__ (self, heading, body):
        self.heading = heading
        self.body = body
        self.confirmed = True

        if self.heading == 'Chance' or self.heading == 'Community Chest':
            self.type = 'confirm'
            self.image = confirmAlertPic
        elif self.heading.__contains__('Tutorial'):
            self.type = 'confirm'
            self.image = confirmAlertPic
        elif self.heading == 'They see me rollin\'' or self.heading == 'Serial doubles-roller' or self.heading == 'Not-so-smooth criminal':
            self.type = 'confirm'
            self.image = confirmAlertPic
        elif self.body.__contains__('?'):
            self.type = 'choice'
            self.image = choiceAlertPic
        elif self.heading == 'Trade':
            self.type = 'trade'
            self.image = tradeAlertPic
        elif self.heading == 'Mortgage' or self.heading == 'Unmortgage' or self.heading == 'Sell house?':
            self.type = 'confirm'
            self.image = confirmAlertPic
        else:
            self.type = 'basic'
            self.image = alertPic
        self.timePausing = 0

    def write(self):
        headingSize = 36
        bodySize = 24
        headingFont = pygame.font.Font('monopoly.ttf', headingSize)
        bodyFont = pygame.font.Font('monopoly.ttf', bodySize)
        lineSpacing = 6

        heading = headingFont.render(self.heading, True, palette.darkGold)

        lines = self.body.split('#')

        screen.blit(self.image, (700, 0))
        screen.blit(heading, (770, 224))
        for i in range(len(lines)):
            lines[i] = bodyFont.render(lines[i], True, palette.axolotl)
            height = 224 + headingSize + lineSpacing + i*(bodySize+lineSpacing)
            screen.blit(lines[i], (770, height))

    def confirmOrDeny(self):
        if self.type == 'choice':
            if inCircle(pygame.mouse.get_pos(), [700+353, 433], 15):
                return 'confirmed'
            if inCircle(pygame.mouse.get_pos(), [700+394, 433], 15):
                return 'denied'
        elif self.type == 'confirm' or self.type == 'trade':
            if inCircle(pygame.mouse.get_pos(), [700 + 394, 433], 15):
                return 'confirmed'
        return False