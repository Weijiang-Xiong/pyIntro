import random, pylab
# vals = []
# for i in range(1000):
#     num1 = random.choice(range(1,200))
#     num2 = random.choice(range(1,200))
#     vals.append(num1 + num2)
# pylab.hist(vals, bins=10)
# pylab.xlabel('number of occurence')
# pylab.show()


# hash table

class intDict(object):
    """A dictionary with integer keys"""
    def __init__(self, numBuckets):
        """Create an empty dictionary"""
        self.buckets = []
        self.numBuckets = numBuckets
        for i in range(numBuckets):
            self.buckets.append([])
    def addEntry(self, key, dictVal):
        """Assumes key an int. Adds an entry."""
        hashBucket = self.buckets[key%self.numBuckets]
        for i in range(len(hashBucket)):
            if hashBucket[i][0] == key:  # if there is already a value corresponding to key, just update the value
                hashBucket[i] = (key, dictVal)
                return
        hashBucket.append((key, dictVal))
    def getValue(self, key):
        """Assumes key an int.
        Returns value associated with key"""
        hashBucket = self.buckets[key%self.numBuckets]
        for e in hashBucket:
            if e[0] == key:
                return e[1]
        return None
    def __str__(self):
        result = '{'
        for b in self.buckets:
            for e in b:
                result = result + str(e[0]) + ':' + str(e[1]) + ','
        return result[:-1] + '}' #result[:-1] omits the last comma

def collisionProb(n, k):
    """Given k randomly picked number that range from i to n, 
    calculate the probability that at least two of them are equal
    """
    prob = 1.0
    for i in range(1, k):
        prob *= ((n-i)/n)
    return 1-prob


D = intDict(17)
for i in range(20):
    #choose a random int in the range 0 to 10**5 - 1
    key = random.choice(range(10**5))
    D.addEntry(key, i)
print('The value of the intDict is:')
print(D)
print('\n', 'The buckets are:')
for hashBucket in D.buckets: #violates abstraction barrier
    print(' ', hashBucket)

