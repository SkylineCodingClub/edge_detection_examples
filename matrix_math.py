#!/usr/bin/python

from numpy import *
from scipy import misc
import matplotlib.pyplot as plt
import copy


def applyKernel(kernel, image):
    new_image = copy.deepcopy(image)
    xOffset = -(math.floor(len(kernel[0]) / 2.0))
    yOffset = -(math.floor(len(kernel) / 2.0))
    imageWidth = len(image[0])
    imageHeight = len(image)
    for image_row in range(len(image)):
        for pixel in range(len(image[image_row])):
            edginess = 0

            for gradient_row in range(len(kernel)):
                for el in range(len(kernel[gradient_row])):
                    if(image_row + gradient_row + xOffset < imageWidth and
                       image_row + gradient_row + xOffset >= 0 and
                       pixel + el + yOffset < imageHeight and
                       pixel + el + yOffset >= 0):
                        value = image[image_row + gradient_row + xOffset][pixel + el + yOffset]
                        intensity = (value * kernel[gradient_row][el])
                        edginess += intensity

            new_image[image_row][pixel] = edginess

    return new_image

# weights array
Xavg = array([[1],
              [2],
              [1]
              ])

# differentiation array
Xdif = array([[-1, 0, +1]])

# weights array
Yavg = array([[1],
              [0],
              [-1],
              ])

# differentiation array
Ydif = array([[1, 2, 1]])

# x kernel
Gx = dot(Xavg, Xdif)

# y kernel
Gy = dot(Yavg, Ydif)

l = misc.imread('lena.png', flatten=1)
lx = applyKernel(Gx, l)
ly = applyKernel(Gy, l)


plt.imshow(hypot(lx, ly), cmap=plt.cm.gray)
plt.show()
