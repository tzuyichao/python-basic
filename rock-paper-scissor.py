class Participant:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.choice = ""
    def choose(self):
        self.choice = input("{name}, select rock, paper or scissor: ".format(name = self.name))
        print("{name} select {choice}".format(name=self.name, choice=self.choice))
    def toNumericalChoice(self):
        switcher = {
            "rock": 0,
            "paper": 1,
            "scissor": 2
        }
        return switcher[self.choice]
    def incrementPoint(self):
        self.points += 1

class GameRound:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        p1.choose()
        p2.choose()
        self.rules = [
            [0, -1, 1],
            [1, 0, -1],
            [-1, 1, 0]
        ]
        result = self.compareChoices()
        print("Round resulted in a {result}".format(result = self.getResultAsString(result)))
        if result > 0:
            p1.incrementPoint()
        elif result < 0:
            p2.incrementPoint()
    def compareChoices(self):
        return self.rules[self.p1.toNumericalChoice()][self.p2.toNumericalChoice()]
    def getResultAsString(self, result):
        res = {
            0: "draw", 
            1: "win",
            -1: "loss"
        }
        return res[result]
    def awardPoints(self):
        print("implement")

class Game:
    def __init__(self) -> None:
        self.endGame = False
        self.participant = Participant("Spock")
        self.secondParticipant = Participant("Kirk")
    def start(self):
        while not self.endGame:
            GameRound(self.participant, self.secondParticipant)
            self.checkEndCondition()
    def checkEndCondition(self):
        answer = input("Continue game y/n: ")
        if answer == 'y':
            GameRound(self.participant, self.secondParticipant)
            self.checkEndCondition()
        else:
            print("Game ended, {p1name} has {p1points}, and {p2name} has {p2points}".format(p1name = self.participant.name, p1points= self.participant.points, p2name=self.secondParticipant.name, p2points=self.secondParticipant.points))
            self.determineWinner()
            self.endGame = True
    def determineWinner(self):
        resultString = "It's a Draw"
        if self.participant.points > self.secondParticipant.points:
            resultString = "Winner is {name}".format(name=self.participant.name)
        elif self.participant.points < self.secondParticipant.points:
            resultString = "Winner is {name}".format(name=self.secondParticipant.name)
        print(resultString)

game = Game()
game.start()
