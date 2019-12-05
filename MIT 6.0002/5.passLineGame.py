import random

def variance(X):
    """Assumes that X is a list of numbers.
    Returns the standard deviation of X"""
    mean = sum(X)/len(X)
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return tot/len(X)

def stdDev(X):
"""Assumes that X is a list of numbers.
Returns the standard deviation of X"""
    return variance(X)**0.5

def rollDie():
    return random.choice([1, 2, 3, 4, 5, 6])

class CrapsGame(object):
    self.passWins = 0
    self.passLoses = 0
    self.dpWins = 0
    self.dpLoses = 0
    self.dpPushes = 0

    def play(self):
        # use a table lookup to replace loops
        pointsDict = {4:1/3, 5:2/5, 6:5/11, 8:5/11, 9:2/5, 10:1/3}
        throw = rollDie() + rollDie()
        if throw == 7 or throw == 11:
            self.passWins += 1
            self.dpLoses += 1
        
        elif throw in [2,3,12]:
            self.passLoses += 1
            if throw ==12:
                self.dpPushes += 1 
            else:
                self.dpWins += 1 
        else:
            if random.random() <= pointsDict[throw]:
                self.passWins += 1
                self.dpLoses += 1
            else:
                self.passLoses += 1
                self.dpWins += 1
            # point = throw
            # while True:
            #     throw = rollDie() + rollDie()
            #     if throw == point:
            #         self.passWins += 1
            #         self.dpLoses += 1
            #         break
            #     elif throw == 7:
            #         self.passLoses += 1
            #         self.dpWins += 1
            #         break

    def passResults(self):
        return (self.passWins, self.passLoses)
    
    def dpResults(self):
        return (self.dpWins, self.dpLoses, self.dpPushes)
        

def crapsSim(handsPerGame, numGames):
    """Assumes handsPerGame and numGames are ints > 0
    Play numGames games of handsPerGame hands; print results"""
    games = []
    #Play numGames games
    for t in range(numGames):
        c = CrapsGame()
        for i in range(handsPerGame):
            c.playHand()
        games.append(c)
    #Produce statistics for each game
    pROIPerGame, dpROIPerGame = [], []
    for g in games:
        wins, losses = g.passResults()
        pROIPerGame.append((wins - losses)/float(handsPerGame))
        wins, losses, pushes = g.dpResults()
        dpROIPerGame.append((wins - losses)/float(handsPerGame))
    #Produce and print summary statistics
    meanROI = str(round((100*sum(pROIPerGame)/numGames), 4)) + '%'
    sigma = str(round(100*stdDev(pROIPerGame), 4)) + '%'
    print('Pass:', 'Mean ROI =', meanROI, 'Std. Dev. =', sigma)
    meanROI = str(round((100*sum(dpROIPerGame)/numGames), 4)) +'%'
    sigma = str(round(100*stdDev(dpROIPerGame), 4)) + '%'
    print('Don\'t pass:','Mean ROI =', meanROI, 'Std Dev =', sigma)

        
