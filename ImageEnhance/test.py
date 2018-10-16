#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-
# Author: Wyundi

# https://blog.csdn.net/guanzhen3657/article/details/81138868

import numpy as np
import cv2 as cv
import os

path1 = "D:\\Project\\Code\\Git\\OpenCV\\ImageEnhance\\OriginImage"
path2 = "D:\\Project\\Code\\Git\\OpenCV\\ImageEnhance\\Enhance"
path2_1 = path2 + "\\" + "2_1"
path2_2 = path2 + "\\" + "2_2"
path2_3 = path2 + "\\" + "2_3"
path2_4 = path2 + "\\" + "2_4"

files= os.listdir(path1)

# 直方图均衡化
def Line(path):
    isExists=os.path.exists(path)
    if isExists == False:
        os.mkdir(path)

    for i in range(len(files)):
        img = cv.imread(path1+'\\'+files[i],1)
        
        hist,bins = np.histogram(img.flatten(),256,[0,256])
        cdf = hist.cumsum()
        cdf_normalized = cdf * float(hist.max()) / cdf.max()
        cdf_m = np.ma.masked_equal(cdf,0)
        cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
        cdf = np.ma.filled(cdf_m,0).astype('uint8')

        img = cdf[img]

        cv.imwrite(path+'\\'+files[i], img)



def main():
    Line(path2_1)

######
main()
######