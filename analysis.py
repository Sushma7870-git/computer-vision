# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 12:48:24 2019

@author: Lenovo
"""

import math
import numpy as np
import imutils
import PIL
from PIL import Image
from matplotlib import pyplot as plt
import cv2
from skimage.morphology import disk
from skimage.filters.rank import gradient

def hist(img):
    img = imutils.resize(img, width=400)
    out1= cv2.split(img)
    col= ['r','g','b']
    #out=cv2.cvtColor( img, cv2.COLOR_HSV2BGR)
    for (i, col) in zip(out1, col):
        hist_o = cv2.calcHist([i], [0], None, [256], [0, 255])   
    
        plt.subplot(111)
        plt.xlim([0, 260])
        plt.xlabel('Grey level',fontsize=20)
        plt.ylabel('Frequency of Pixels',fontsize=20)
        plt.plot(hist_o,color=col)
        plt.title('histogram',fontsize=20)    
    plt.show()

def cdf(data):
    pixels = data.flatten()
    xs = np.sort(pixels)
    ys= np.arange(1,len(xs)+1)/len(xs)
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111)
    ax.grid(True)
    #ax.plot(xs,d, '-r', label="linear")
    ax.plot(xs,ys, 'k-', label="Original")
    ax.set_title('CDF of histogram',fontsize=20)
    ax.set_xlim([xs.min(), xs.max()])
    ax.legend(loc=2)
    ax.set_xlabel('Grey intensity level',fontsize=20)
    ax.set_ylabel('Cummulative sum',fontsize=20)
    
def entropy(img):
    gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gray,(960,540))
    selection_element = disk(5) # matrix of n pixels with a disk shape
    cat_sharpness = gradient(gray, selection_element)
    plt.imshow(cat_sharpness, cmap="viridis")
    plt.axis('off')
    plt.colorbar()
    plt.show()  
    
if __name__ == '__main__':
    
img = cv2.imread(r'path of image')# give the full path of test image
hist(img)
entropy(img)
cdf(img)