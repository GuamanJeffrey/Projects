#Name: Jeffrey Guaman
#Email: JEFFREY.GUAMAN18@myhunter.cuny.edu
#Date: October 5th, 2023
#This program crops a picture to only show a quarter of the pic. 
import matplotlib.pyplot as plt
import numpy as np
x = input("Enter a image file: ")
y = input("Enter an output file: ")

img = plt.imread(x)

size = img.shape

h = size[0]
w = size[1]

halfh = int(size[0]) // 2
halfw = int(size[1]) // 2


img2 = img[halfh:,:halfw]

plt.imsave(y, img2)
