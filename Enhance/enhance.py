# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 14:05:38 2019

@author: Lenovo
"""

import cv2
import numpy as np
import math


def Enhance(img):
    contrast = 1.3
    clahe = cv2.createCLAHE(clipLimit=2, tileGridSize=(8,8))
    img =cv2.resize(img,(640,480))
    img_hsv= cv2.cvtColor(img, cv2.COLOR_BGR2HSV) 
    H,S,V = cv2.split(img_hsv)
    
    V_C = clahe.apply(V)
    def loop(R):
        height_R=R.shape[0]
        width_R=R.shape[1]
        for i in np.arange(height_R):
            for j in np.arange(width_R):
                a = R.item(i,j)
                b = math.ceil(a * contrast)
                if b > 255:
                    b = 255
                R.itemset((i,j), b)
        return R
    HSV = cv2.merge((H,S,V_C))
    output= cv2.cvtColor(HSV , cv2.COLOR_HSV2BGR)
    B,G,R = cv2.split(output)
    B=loop(B)
    G=loop(G)
    R=loop(R)
    OUTPUT1 = cv2.merge((B,G,R))
    return OUTPUT1
if __name__ == '__main__':
    img= cv2.imread(r'input\foggy.JPG')
    enhanced= Enhance(img)
    cv2.imshow('contrast enhanced image', enhanced)
    cv2.imwrite(r'output\cont_enhanced.JPG',enhanced)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
     


