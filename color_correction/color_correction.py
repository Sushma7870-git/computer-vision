                                            # -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 16:38:54 2019

@author: Lenovo
"""

import cv2
import math
import numpy as np
import imutils
from matplotlib import pyplot as plt

plt.rcParams["font.family"] = "Times New Roman"  

def apply_mask(matrix, mask, fill_value):
    masked = np.ma.array(matrix, mask=mask, fill_value=fill_value)
    return masked.filled()
    print(masked)
   
def apply_threshold(matrix, low_value, high_value):
    low_mask = matrix < low_value
    matrix = apply_mask(matrix, low_mask, low_value)

    high_mask = matrix > high_value
    matrix = apply_mask(matrix, high_mask, high_value)
    print('...........aaaa')
    print(matrix)
    return matrix

def simplest_cb(img, percent):
    assert img.shape[2] == 3
    assert percent > 0 and percent < 100

    half_percent = percent / 200.0
    #img=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    channels = cv2.split(img)

    out_channels = []
    for channel in channels:
        assert len(channel.shape) == 2
        # find the low and high precentile values (based on the input percentile)
        height, width = channel.shape
        vec_size = width * height
        flat = channel.reshape(vec_size)

        assert len(flat.shape) == 1

        flat = np.sort(flat)

        n_cols = flat.shape[0]

        low_val  = flat[math.floor(n_cols * half_percent)]
        high_val = flat[math.ceil( n_cols * (1.0 - half_percent))]

        #print "Lowval: ", low_val
        #print "Highval: ", high_val

        # saturate below the low percentile and above the high percentile
        thresholded = apply_threshold(channel, low_val, high_val)
        # scale the channel
        normalized = cv2.normalize(thresholded, thresholded.copy(), 0, 255, cv2.NORM_MINMAX)
        out_channels.append(normalized)

    return cv2.merge(out_channels)

if __name__ == '__main__':
    img = cv2.imread(r'F:\S.K\python\color_correction\test_images\2.2.JPG')
    img = imutils.resize(img, width=400)
    img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    out = simplest_cb(img, 1)
    out1= cv2.split(out)
    col= ['r','g','b']
    for (i, col) in zip(out1, col):
        hist_o = cv2.calcHist([i], [0], None, [256], [0, 255])   
    
        plt.subplot(111)
        plt.xlim([0, 260])
        plt.xlabel('Grey level',fontsize=20)
        plt.ylabel('Frequency of Pixels',fontsize=20)
        plt.plot(hist_o,color=col)
        plt.title('Color_corrected_histogram',fontsize=20)    
    plt.show()
    fig, (ax0, ax1) = plt.subplots(ncols=2, figsize=(12, 8),
                                   sharex=True, sharey=True)
    
    img0 = ax0.imshow(img)# cmap=plt.cm.gray)
    ax0.set_title("Before")
    ax0.axis("off")
    #fig.colorbar(img0, ax=ax0)
    
    img2 = ax1.imshow(out)# cmap="viridis")
    ax1.set_title("After")
    ax1.axis("off")
   # fig.colorbar(img2, ax=ax1)
    
    fig.tight_layout()
    
    plt.show()
    