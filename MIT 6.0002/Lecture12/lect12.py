#%%
# addpath python version
import sys
sys.path.append('F:/7_Myworks/pyintro/6-0002-fall-2016/Lecture12')

import cluster
import random, pylab, numpy

#%%
class Patient(cluster.Example):
    pass

def scaleAttrs(vals):
    """scale the input vals to have zero mean and 1 variance
    """
    vals = pylab.array(vals)
    mean = sum(vals)/len(vals)
    sd = numpy.std(vals)
    vals = vals - mean
    return vals/sd

def getData(toScale = False):
    #read in data
    hrList, stElevList, ageList, prevACSList, classList = [],[],[],[],[]
    # even if sys.path contains the directory of lect12.py, 
    # when calling 'open', vscode still searches files in 'pyintro', which 
    # is the folder opened in vscode. so pay attention to it..
    cardiacData = open('./6-0002-fall-2016/Lecture12/cardiacData.txt', 'r')
    for l in cardiacData:
        l = l.split(',')
        hrList.append(int(l[0]))
        stElevList.append(int(l[1]))
        ageList.append(int(l[2]))
        prevACSList.append(int(l[3]))
        classList.append(int(l[4]))
    if toScale:
        hrList = scaleAttrs(hrList)
        stElevList = scaleAttrs(stElevList)
        ageList = scaleAttrs(ageList)
        prevACSList = scaleAttrs(prevACSList)
    #Build points
    points = []
    for i in range(len(hrList)):
        features = pylab.array([hrList[i], prevACSList[i], stElevList[i], ageList[i]])
        pIndex = str(i)
        points.append(Patient('P'+ pIndex, features, classList[i]))
    return points
    
def kmeans(examples, k, verbose = False):
    #Get k randomly chosen initial centroids, create cluster for each
    initialCentroids = random.sample(examples, k)
    clusters = []
    for e in initialCentroids:
        clusters.append(cluster.Cluster([e]))
        
    #Iterate until centroids do not change
    converged = False
    numIterations = 0
    while not converged:
        numIterations += 1
        #Create a list containing k distinct empty lists
        newClusters = []
        for i in range(k):
            newClusters.append([])
            
        #Associate each example with closest centroid
        for e in examples:
            #Find the centroid closest to e
            smallestDistance = e.distance(clusters[0].getCentroid())
            index = 0
            for i in range(1, k):
                distance = e.distance(clusters[i].getCentroid())
                if distance < smallestDistance:
                    smallestDistance = distance
                    index = i
            #Add e to the list of examples for appropriate cluster
            newClusters[index].append(e)
            
        for c in newClusters: #Avoid having empty clusters
            if len(c) == 0:
                try:
                    newClusters.remove(c)
                except:     
                    raise ValueError('Empty Cluster')
        
        #Update each cluster; check if a centroid has changed
        converged = True
        for i in range(k):
            if clusters[i].update(newClusters[i]) > 0.0:
                converged = False
        if verbose:
            print('Iteration #' + str(numIterations))
            for c in clusters:
                print(c)
            print('') #add blank line
    return clusters

def trykmeans(examples, numClusters, numTrials, verbose = False):
    """Calls kmeans numTrials times and returns the result with the
          lowest dissimilarity"""
    best = kmeans(examples, numClusters, verbose)
    minDissimilarity = cluster.dissimilarity(best)
    trial = 1
    while trial < numTrials:
        try:
            clusters = kmeans(examples, numClusters, verbose)
        except ValueError:
            continue #If failed, try again
        currDissimilarity = cluster.dissimilarity(clusters)
        if currDissimilarity < minDissimilarity:
            best = clusters
            minDissimilarity = currDissimilarity
        trial += 1
    return best

def printClustering(clustering):
    """Assumes: clustering is a sequence of clusters
       Prints information about each cluster
       Returns list of fraction of pos cases in each cluster"""
    posFracs = []
    for c in clustering:
        numPts = 0
        numPos = 0
        for p in c.members():
            numPts += 1
            if p.getLabel() == 1:
                numPos += 1
        fracPos = numPos/numPts
        posFracs.append(fracPos)
        print('Cluster of size', numPts, 'with fraction of positives =',
              round(fracPos, 4))
    return pylab.array(posFracs)

def testClustering(patients, numClusters, seed = 0, numTrials = 5):
    random.seed(seed)
    bestClustering = trykmeans(patients, numClusters, numTrials)
    posFracs = printClustering(bestClustering)
    return posFracs

# patients = getData()
# for k in (2,): # the comma means type tuple
#     print('\n     Test k-means (k = ' + str(k) + ')')
#     posFracs = testClustering(patients, k, 2)

#numPos = 0
#for p in patients:
#    if p.getLabel() == 1:
#        numPos += 1
#print('Total number of positive patients =', numPos)


def genDistribution(xMean, xSD, yMean, ySD, n, namePrefix):
    samples = []
    for s in range(n):
        x = random.gauss(xMean, xSD)
        y = random.gauss(yMean, ySD)
        samples.append(cluster.Example(namePrefix+str(s), [x, y]))
    return samples


def plotSamples(samples, marker):
    xVals, yVals = [], []
    for s in samples:
        x = s.getFeatures()[0]
        y = s.getFeatures()[1]
        pylab.annotate(s.getName(), xy = (x, y),
        xytext = (x+0.13, y-0.07),
        fontsize = 'x-large')
        xVals.append(x)
        yVals.append(y)
    pylab.plot(xVals, yVals, marker)
    
def contrivedTest(numTrials, k, verbose = False):
    xMean = 3
    xSD = 1
    yMean = 5
    ySD = 1
    n = 10
    d1Samples = genDistribution(xMean, xSD, yMean, ySD, n, 'A')
    plotSamples(d1Samples, 'k^')
    d2Samples = genDistribution(xMean+3, xSD, yMean+1, ySD, n, 'B')
    plotSamples(d2Samples, 'ko')
    clusters = trykmeans(d1Samples+d2Samples, k, numTrials, verbose)
    print('Final result')
    for c in clusters:
        print('', c)


def contrivedTest2(numTrials, k, verbose = False):
    xMean = 3
    xSD = 1
    yMean = 5
    ySD = 1
    n = 8
    d1Samples = genDistribution(xMean,xSD, yMean, ySD, n, 'A')
    plotSamples(d1Samples, 'k^')
    d2Samples = genDistribution(xMean+3,xSD,yMean, ySD, n, 'B')
    plotSamples(d2Samples, 'ko')
    d3Samples = genDistribution(xMean, xSD, yMean+3, ySD, n, 'C')
    plotSamples(d3Samples, 'kx')
    clusters = trykmeans(d1Samples + d2Samples + d3Samples, k, numTrials, verbose)
    pylab.ylim(0,11)
    print('Final result has dissimilarity',round(cluster.dissimilarity(clusters), 3))
    for c in clusters:
        print(" ",c)
        
contrivedTest2(40, 2)


