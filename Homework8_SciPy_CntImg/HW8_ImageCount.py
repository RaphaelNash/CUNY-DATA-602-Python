import scipy.ndimage as ndi
import scipy.misc as misc
from skimage import feature, measure
from skimage import morphology
import numpy as np
import matplotlib.pyplot as plt

import scipy
from scipy import ndimage


"""
In this assignment we are counting the number of objects in an imange and geting the centerpoints
"""

print"Finding centers for circles.png"
circles = scipy.misc.imread('./circles.png')

circlesf = ndimage.gaussian_filter( circles, 3)

labeled, nr_objects = ndimage.label(circlesf  ) # `dna[:,:,0]>T` for red-dot case
print "Number of circles is %d " % nr_objects
print "Centers for circles are:"
print ndimage.measurements.center_of_mass( circlesf, labeled, range(1,nr_objects+1))

print"---------------"

print"Finding centers for objects.png"
objects  = scipy.misc.imread('./objects.png') # gray-scale image
objectsf = ndimage.gaussian_filter(objects, 3)
objectst = objectsf > objectsf.mean()
labeled, nr_objects = ndimage.label(objectst ) # `dna[:,:,0]>T` for red-dot case
print "Number of objects are %d " % nr_objects
print "Centers of objects are:"
print ndimage.measurements.center_of_mass( objectst, labeled, range(1,nr_objects+1))


print"---------------"

print"Finding centers for pepers.png"
objects  = scipy.misc.imread('./peppers.png') # gray-scale image
objectsf = ndimage.gaussian_filter(objects, 6)
objectst = objectsf > objectsf.mean()
labeled, nr_objects = ndimage.label(objectst )
print "Number of peppers are %d " % nr_objects
print "Centers for pepers are:"
print ndimage.measurements.center_of_mass( objectst, labeled, range(1,nr_objects+1))


