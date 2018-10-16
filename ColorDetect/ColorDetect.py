# !/usr/bin/env python
# -  *  - coding:utf-8 -  *  - 
# Author:Wyundi

import numpy as np
import cv2 as cv

# HSV颜色区间
##################################
red_min = np.array([0, 128, 46])
red_max = np.array([5, 255, 255])
red2_min = np.array([156, 128, 46])
red2_max = np.array([180, 255, 255])

green_min = np.array([35, 128, 46])
green_max = np.array([77, 255, 255])

blue_min = np.array([100, 128, 46])
blue_max = np.array([124, 255, 255])

yellow_min = np.array([15, 128, 46])
yellow_max = np.array([34, 255, 255])

black_min = np.array([0, 0, 0])
black_max = np.array([180, 255, 50])

white_min = np.array([0, 0, 70])
white_max = np.array([180, 30, 255])
######################################

cap = cv.VideoCapture(0)


# 颜色检测函数
def checkImage(imgHSV):
    # 去除噪点
    mask_black = cv.inRange(imgHSV, black_min, black_max)          # 二值化（参数：图像，HSV颜色下限，上限）
    kernel = np.ones((3, 3), np.uint8)                          # 卷积核
    # mask_black = cv.erode(mask_black, None, iterations = 2)       # 腐蚀（参数：图像，卷积核，卷积次数）
    # mask_black = cv.dilate(mask_black, kernel, iterations = 1)    # 膨胀（参数：图像，卷积核，卷积次数）
    # center location
    if (mask_black == 255).any():
        CY, CX = np.where(mask_black == 255)
        x = np.mean(CX)
        y = np.mean(CY)                                         # x, y为中心点坐标
        # 绘制中心点
        cv.circle(mask_black, (int(x), int(y)), 5, (100, 100, 100), -1)

    cv.imshow('black', mask_black)                                # 显示当前帧（mask）


while (True):
    ret, frame = cap.read()                                     # 截取图像

    VIDEO = cv.cvtColor(frame, cv.COLOR_BGR2BGRA)               # VIDEO->BGRA显示
    imgHSV = cv.cvtColor(frame, cv.COLOR_BGR2HSV)               # imgHSV->HSV显示

    checkImage(imgHSV)                                          # 颜色检测

    cv.imshow('frame', VIDEO)                                   # 显示当前帧（VIDEO）
    if cv.waitKey(1) & 0xFF == ord('q'):                        # 按键检测 按q退出
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()