#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-
# Author: Wyundi

import numpy as np
import cv2 as cv
import os

path1 = "C:\\1"
path2 = "C:\\2"
path2_1 = "C:\\2\\1"
path2_2 = "C:\\2\\2"
path2_3 = "C:\\2\\3"
path2_4 = "C:\\2\\4"

files= os.listdir(path1)

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