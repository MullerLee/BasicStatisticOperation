#-*- encoding utf-8 -*-
"""
    @ file: image_pre_processor.py
    @ author: X.C.Lee
    @ date: 8/30/2018
"""

import matplotlib
import matplotlib.pyplot as plt 
import matplotlib.image as img

def TwoDim_LPFilter(prearr, threshold):  # Two-Dimention Low Pass Filter, 0 < threshold < 255
    array=prearr
    i=0
    j=0
    while i<array.shape[0]:
        while j<array.shape[1]:
            if array[i][j]>threshold:
                array[i][j]=0
            j=j+1
        j=0
        i=i+1
    i=0                                     #stack protect
    return array

def TwoDim_HPFilter(prearr, threshold):  # Two-Dimention High Pass Filter, 0 < threshold < 255
    array=prearr
    i=0
    j=0
    while i<array.shape[0]:
        while j<array.shape[1]:
            if array[i][j]<threshold:
                array[i][j]=0
            j=j+1
        j=0
        i=i+1
    i=0                                     #stack protect
    return array


 # Two-Dimention Band Pass Filter, 0 < thresholdL< thresholdH< 255

def TwoDim_BPFilter(prearr, thresholdL, thresholdH):
    array=prearr
    i=0
    j=0
    while i<array.shape[0]:
        while j<array.shape[1]:
            if array[i][j]<thresholdL | array[i][j]>thresholdH :
                array[i][j]=0
            j=j+1
        j=0
        i=i+1
    i=0                                     #stack proteck
    return array

# Fuzzificate the edge of two objects in rows, 0 < threshold < 255
def TwoDim_FuzEdgeRow_Filter(prearr,threshold):
    array=prearr
    i=0
    j=0
    while i<array.shape[0]-1:
        while j<array.shape[1]-1:
            div=0
            if array[i][j]>array[i][j+1]:
                div=array[i][j]-array[i][j+1]
            else:
                div=array[i][j+1]-array[i][j]
            if div>threshold:
                array[i][j]=array[i][j+1]/2+array[i][j]/2
            j=j+1
        j=0
        i=i+1
    i=0                                     #stack proteck
    return array

# Fuzzificate the edge of two objects in coloums, 0 < threshold < 255
def TwoDim_FuzEdgeCol_Filter(prearr,threshold):
    array=prearr
    i=1
    j=0
    while i<array.shape[0]-1:
        while j<array.shape[1]-1:
            div=0
            if array[i][j]>array[i-1][j]:
                div=array[i][j]-array[i-1][j]
            else:
                div=array[i-1][j]-array[i][j]
            if div>threshold:
                array[i][j]=array[i-1][j]/2+array[i][j]/2
            j=j+1
        j=0
        i=i+1
    i=0                                     #stack proteck
    return array

def TwoDim_Diverse(prearr):
    array=prearr
    i=0
    j=0
    while i<array.shape[0]:
        while j<array.shape[1]:
            array[i][j]=255-array[i][j]
            j=j+1
        j=0
        i=i+1
    i=0                                     #stack proteck
    return array

# test code
image=img.imread("C:\\Users\\The Eternal\\Pictures\\th.jpg") #pictures in any path's okay
#car_out=TwoDim_BPFilter(image[:,:,0],100,200)
#peo_out=TwoDim_FuzEdgeCol_Filter(image[:,:,0],5)
#peo_out2=TwoDim_FuzEdgeCol_Filter(peo_out,5)
peo_out3=TwoDim_Diverse(image[:,:,0])
plt.imshow(image[:,:,0],cmap='Greys_r')
plt.show()
#print(car_out)
