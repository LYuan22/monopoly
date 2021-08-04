class TaxSquares: # Again, more of an identifier than anything else.
    def __init__(self, name, boardpos):
        self.name = name
        self.boardpos = boardpos
        self.paid = False

    def getTax(self):
        if self.name == 'Income Tax':
            return 200
        return 100

class SpecialSquares: # Applies to the squares on the corners.
    def __init__(self, name, boardpos):
        self.name = name
        self.boardpos = boardpos
        self.paid = False

    def getPayAmount(self): # Returns how much money a player gets for landing on a square. See Alert classes for details on alerts
        global alert
        if self.name == 'Go':
            if user.isTurn:
                alert = Alert('Lazy Programming', 'You landed on Go and got $400 #because I was too lazy to fix #that issue. Some people play by #that rule anyway.')
            elif Eve.isTurn:
                alert = EveAlert('Sweet sweet cashola', 'Eve gets $400 by landing on Go')

            return 200
        elif self.name == 'Free Parking':
            if user.isTurn:
                alert = Alert("It's Free Parking")
        else:
            return 0