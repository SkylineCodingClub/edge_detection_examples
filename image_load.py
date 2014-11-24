#!/usr/bin/perl

import matplotlib.pyplot as plt
import numpy
from scipy import misc
from scipy import ndimage
l = misc.imread('lena.png', flatten=1)

sx = ndimage.sobel(l, axis=0, mode='constant')
sy = ndimage.sobel(l, axis=1, mode='constant')
sob = numpy.hypot(sx, sy)
plt.imshow(sob, cmap=plt.cm.gray)
plt.show()
