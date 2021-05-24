#Liz L., Mike Mehr, Will Rushton, Sam Goodin

class TicTacToe:

    def __init__(self):
        self.first = "O"
        self.resetGame()
        self.xpoints, self.opoints = 0, 0
        while 1:
            choice = self.playGame()
            if choice.lower() == "n":
                break
            else:
                self.resetGame()

    def playGame(self):
        while not self.win:
            self.displayBoard()
            spot = int(input("{0}'s turn. Where would you like to move? ".format(self.turn)))
            if spot in self.spotsUsed:
                print("That spot is already taken. Choose another.")
            else:
                self.updateBoard(spot)
                self.checkWin()
                if self.turn == "X":
                    self.turn = "O"
                else:
                    self.turn = "X"
                if self.counter != 9:
                    self.counter += 1
                else:
                    break
        return input("Would you like to play again? (Y or N) ")

    def updateBoard(self, spot):
        if spot is 1:
            self.spot1 = "_{0}_".format(self.turn)
        elif spot is 2:
            self.spot2 = "_{0}_".format(self.turn)
        elif spot is 3:
            self.spot3 = "_{0}_".format(self.turn)
        elif spot is 4:
            self.spot4 = "_{0}_".format(self.turn)
        elif spot is 5:
            self.spot5 = "_{0}_".format(self.turn)
        elif spot is 6:
            self.spot6 = "_{0}_".format(self.turn)
        elif spot is 7:
            self.spot7 = "_{0}_".format(self.turn)
        elif spot is 8:
            self.spot8 = "_{0}_".format(self.turn)
        elif spot is 9:
            self.spot9 = "_{0}_".format(self.turn)
        self.spotsUsed.append(spot)

    def checkWin(self):
        if self.spot1 == "_{0}_".format(self.turn) and self.spot2 == "_{0}_".format(self.turn) and self.spot3 == "_{0}_".format(self.turn):
            self.win()
        elif self.spot4 == "_{0}_".format(self.turn) and self.spot5 == "_{0}_".format(self.turn) and self.spot6 == "_{0}_".format(self.turn):
            self.win()
        elif self.spot7 == "_{0}_".format(self.turn) and self.spot8 == "_{0}_".format(self.turn) and self.spot9 == "_{0}_".format(self.turn):
            self.win()
        elif self.spot1 == "_{0}_".format(self.turn) and self.spot4 == "_{0}_".format(self.turn) and self.spot7 == "_{0}_".format(self.turn):
            self.win()
        elif self.spot2 == "_{0}_".format(self.turn) and self.spot5 == "_{0}_".format(self.turn) and self.spot8 == "_{0}_".format(self.turn):
            self.win()
        elif self.spot3 == "_{0}_".format(self.turn) and self.spot6 == "_{0}_".format(self.turn) and self.spot9 == "_{0}_".format(self.turn):
            self.win()
        elif self.spot1 == "_{0}_".format(self.turn) and self.spot5 == "_{0}_".format(self.turn) and self.spot9 == "_{0}_".format(self.turn):
            self.win()
        elif self.spot3 == "_{0}_".format(self.turn) and self.spot5 == "_{0}_".format(self.turn) and self.spot7 == "_{0}_".format(self.turn):
            self.win()

    def win(self):
        self.win = True
        print("Congrats! Player {0} wins!".format(self.turn))
        if self.turn == "X":
            self.xpoints += 1
        else:
            self.opoints += 1

    def resetGame(self):
        self.spot1 = "(1)"
        self.spot2 = "(2)"
        self.spot3 = "(3)"
        self.spot4 = "(4)"
        self.spot5 = "(5)"
        self.spot6 = "(6)"
        self.spot7 = "(7)"
        self.spot8 = "(8)"
        self.spot9 = "(9)"
        self.win = False
        if self.first == "O":
            self.turn = "X"
            self.first = "X"
        else:
            self.turn = "O"
            self.first = "O"
        self.counter = 1
        self.spotsUsed = []

    def displayBoard(self):
        print("""
{0}|{1}|{2}
{3}|{4}|{5}
{6}|{7}|{8}

Points:
X: {9}  O: {10}
""".format(self.spot1, self.spot2, self.spot3, self.spot4, self.spot5, 
           self.spot6, self.spot7, self.spot8, self.spot9, self.xpoints, self.opoints))

TicTacToe()