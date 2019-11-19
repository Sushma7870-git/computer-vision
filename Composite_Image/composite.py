# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 16:58:13 2019

@author: Lenovo
"""

import cv2
#read background, forground, and mask.
top=cv2.imread(r'input\comp_foreground.jpg')
mask=cv2.imread(r'input\comp_mask.jpg')
img=cv2.imread(r'input\comp_background.jpg')
#invert the mask
mask_inv= ~mask
forg=mask & top
back=mask_inv & img
result=back + forg
#cv2.imshow('forg',forg)
#cv2.imshow('back',back)
cv2.imshow('result',result)
#cv2.imwrite(r'output\composite.jpg',result)
cv2.waitKey(0)
cv2.destroyAllWindows()
