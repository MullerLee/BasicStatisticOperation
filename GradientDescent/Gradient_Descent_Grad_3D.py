#-*- encoding utf-8 -*-
# File name: Gradient_Descent.py
# Author: Muller Lee (X.C.Lee)
# Date: 2018/7/8

import numpy as np
import math
import matplotlib
import matplotlib.pyplot as plt
import random
from mpl_toolkits.mplot3d import Axes3D

'''
Global variables
'''
test_list=[[1,3],[2,4],[3,3],[5,6],[3,8],[2,5],[5,10],[6,8],[6,7],[7,6],[7,8],[10,11],[10,9],[9,9],[8,9],[2,1],[3,3],[5,8],[10,12],[12,11],[13,15],[11,13],[12,16]]
regre_var_1=random.randint(-5,0)
regre_var_2=random.randint(0,5)

test_list_x=[0]
test_list_y=[0]
diss=[0]

expect=10000
pre_expect=10000
error=1000

x_bar=0
y_bar=0
all_count=0
'''
function
'''

'''
main
'''
count1=0

for element in test_list:
	x_bar=x_bar+element[0]
	y_bar=y_bar+element[1]
	count1=count1+1
x_bar=x_bar/count1
y_bar=y_bar/count1

print(regre_var_1,regre_var_2,error)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.ion()
while 1:
	test_list_x=[0]
	test_list_y=[0]
	diss=[0]
	all_count=all_count+1
	#print("--")
	for elem in test_list:
		test_list_x.append(elem[0])
		test_list_y.append(elem[1])
		diss.append((elem[0]*regre_var_1-elem[1]+regre_var_2)*(elem[0]*regre_var_1-elem[1]+regre_var_2)/(regre_var_1*regre_var_1+1))
		
	summ=0.0
	count=-1
	for rec in diss:
		summ=summ+rec
		count=count+1
	##stop point
	pre_expect=expect
	expect=summ/(count)
	error=pre_expect-expect
	if (error<0.001 and error>0) or all_count>10000:
		break
	
	#x=np.arange(0, 15.0, 0.01)
	#x=np.arange(-5, 10.0, 0.01)
	#y=regre_var_1*x+regre_var_2
	#draw point


	#print("0000000")

	a=regre_var_1
	b=regre_var_2
	regre_var_1=a-0.01*(2*(a*x_bar-y_bar+b)/(a*a+1))
	regre_var_2=b-0.01*2*(x_bar-y_bar+b)/(a*a+1)
	
	print(regre_var_1,regre_var_2,error)
	'''
	for elem in test_list:
		plt.scatter(elem[0],elem[1],s=5,edgecolors='None',c='blue')
	'''
	#plt.scatter(x,y,s=1,edgecolors='None',c='red')
	ax.scatter(regre_var_1,regre_var_2,expect,c='r', marker='o')
	ax.set_xlabel('a')
	ax.set_ylabel('b')
	ax.set_zlabel('distance')
	plt.pause(0.00001)
	#plt.cla()
	plt.show()

print(regre_var_1,regre_var_2,error)
'''
x=np.arange(0, 15.0, 0.01)
y=regre_var_1*x+regre_var_2
for elem in test_list:
	plt.scatter(elem[0],elem[1],s=5,edgecolors='None',c='blue')
plt.scatter(x,y,s=1,edgecolors='None',c='red')
plt.show()
'''

#plt.savefig(('D:/MyFig.jpg')
