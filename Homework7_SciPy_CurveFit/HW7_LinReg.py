import timeit
setup = '''

import numpy as np
from scipy.optimize import curve_fit

class BrainBody(object):
    def __init__(self, line):
        line_parsed = line.split(",")
        self.species = line_parsed[0]
        self.body = float(line_parsed[1])
        self.brain = float(line_parsed[2])


def linear_func(x, a, b):
    return a * x + b

def least_sq(brain_body_list, print_output):
    n =  len(brain_body_list)

    sigma_X = 0.0
    sigma_Y = 0.0
    sigma_XY = 0.0
    sigma_X2 = 0.0

    for brain_body_item in brain_body_list:
        sigma_X += brain_body_item.brain
        sigma_Y += brain_body_item.body
        sigma_XY +=  (brain_body_item.body * brain_body_item.brain)
        sigma_X2 += (brain_body_item.brain * brain_body_item.brain)

    slope = ((n*sigma_XY) - (sigma_X*sigma_Y)) / ( n * sigma_X2 - (sigma_X*sigma_X))
    intercept  = (sigma_Y - (slope*sigma_X) ) / n

    if( print_output):
        print ("Least Squares: ")
        print "slope: "  + str(slope)
        print "intercept: " + str(intercept)
        print ""
        print "body = " + str(round(slope,2)) + " * brain + " + str(round(intercept,2))

def sci_py_lin_curve_fit(brain_body_list, print_output):
    body = []
    brain = []

    for brain_body_item in brain_body_list:
        body.append(brain_body_item.body)
        brain.append(brain_body_item.brain)


    popt, pcov = curve_fit(linear_func, brain, body)

    if( print_output):
        print(popt)
        print ("")
        print("SciPy Curve Fit:")
        print("body =  %f * x  + %f") % (popt[0], popt[1])

brain_body_list = []
in_file = open("brainandbody.csv", "r")
lines = in_file.read().splitlines()
for line in lines:
    if line[:1] != ",":         #ignore first row as it is just a header
        brain_body_item = BrainBody(line)
        brain_body_list.append(brain_body_item)

in_file.close()
'''



#run for timings
n=1000
t=timeit.Timer('sci_py_lin_curve_fit(brain_body_list, False)', setup=setup)
print"Time with Sci Py: ", t.timeit(1000)
t=timeit.Timer('least_sq(brain_body_list, False)', setup=setup)
print"Time with Least Sq: ", t.timeit(1000)

print
print

#run for output
t=timeit.Timer('least_sq(brain_body_list, True)', setup=setup)
t.timeit(1)
t=timeit.Timer('sci_py_lin_curve_fit(brain_body_list, True)', setup=setup)
t.timeit(1)
