# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 12:48:24 2019

@author: Lenovo
"""

import numpy as np
import imutils
from matplotlib import pyplot as plt
import cv2
from skimage.morphology import disk
from skimage.filters.rank import gradient
from skimage.util import img_as_ubyte
from skimage.filters.rank import entropy

def hist(img):
    img = imutils.resize(img, width=400)
    out1= cv2.split(img)
    col= ['r','g','b']
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
    
def Entropy(img):
    img=cv2.cvtColor( img, cv2.COLOR_BGR2GRAY)
    img1 = img_as_ubyte(img)

    fig, (ax0, ax1) = plt.subplots(ncols=2, figsize=(12, 4),
                                   sharex=True, sharey=True)
    
    img0 = ax0.imshow(img1, cmap=plt.cm.gray)
    ax0.set_title("Original_Image")
    ax0.axis("off")
    fig.colorbar(img0, ax=ax0)
    ent= entropy(img1, disk(5))
    img2 = ax1.imshow(ent, cmap="viridis")
    ax1.set_title("Entropy")
    ax1.axis("off")
    fig.colorbar(img2, ax=ax1)
    
    fig.tight_layout()
    
    plt.show()
    
if __name__ == '__main__':
    
    img = cv2.imread(r'Test_images\idol.jpg')# give the full path of test image
    hist(img)
    Entropy(img)
    cdf(img)