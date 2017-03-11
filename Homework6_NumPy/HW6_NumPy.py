
import timeit
import random

setup = '''
import numpy
import copy
import random

def sortwithloops(input):
        for i in range(1, len(input)):
            while input[i - 1] > input[i] and i >= 0:
                input[i - 1], input[i] = input[i], input[i - 1]
                i -= 1
        return input



def sortwithoutloops(input):
    return sorted(input)

def sortwithnumpy (input):
    return numpy.sort(input)



def searchwithloops(input, value):
    for i in input:
        if i == value:
            return True
    return False

def searchwithoutloops(input, value):
    if value in input:
        return True

    return False

def searchwithnumpy(input, value):
    if numpy.any(input == value) :
        return True
    else:
        return False

randomList = random.sample(xrange(1000), 1000)
randomListNumpy = numpy.array(randomList)
'''



n=100
t = timeit.Timer("x=copy.copy(randomList); sortwithloops(x) ", setup=setup)
print "Sort with loops time = ", t.timeit(n)
t = timeit.Timer("x=copy.copy(randomList); sortwithoutloops(x) ", setup=setup)
print "Sort without loops time = ", t.timeit(n)
t = timeit.Timer("x=copy.copy(randomListNumpy); sortwithnumpy(x) ", setup=setup)
print "Sort with numpy time = ", t.timeit(n)
print("")
t = timeit.Timer("x=copy.copy(randomList); searchwithloops(x,random.randint(0,1000)) ", setup=setup)
print "Search with loops time = ", t.timeit(n)
t = timeit.Timer("x=copy.copy(randomList); searchwithoutloops(x, random.randint(0,1000)) ", setup=setup)
print "Search without loops time = ", t.timeit(n)
t = timeit.Timer("x=copy.copy(randomListNumpy); searchwithnumpy(x, random.randint(0,1000)) ", setup=setup)
print "Search with numpy time = ", t.timeit(n)



