import random
import pylab

def flipPlot(minExp, maxExp):
    ratios, diffs, xAxis = [], [], []
    for exp in range(minExp, maxExp + 1):
        xAxis.append(2**exp)
    for numFlips in xAxis:
        numHeads = 0
        for n in range(numFlips):
            if random.choice(('H', 'T')) == 'H':
                numHeads += 1
        numTails = numFlips - numHeads
        try:
            ratios.append(numHeads/numTails)
            diffs.append(abs(numHeads - numTails))
        except ZeroDivisionError:
            continue
    pylab.title('Difference Between Heads and Tails')
    pylab.xlabel('Number of Flips')
    pylab.semilogx()
    pylab.semilogy()
    pylab.ylabel('Abs(#Heads - #Tails)')
    # pylab.plot(xAxis, diffs, 'k')
    pylab.scatter(xAxis, diffs)
    pylab.figure()
    pylab.title('Heads/Tails Ratios')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('#Heads/#Tails')
    pylab.semilogx()
    pylab.semilogy()
    # pylab.plot(xAxis, ratios, 'k')
    pylab.scatter(xAxis, ratios, c='k')
    pylab.show()

def main():
    random.seed(0)
    flipPlot(4, 20)

if __name__ == "__main__":
    main()