#-*- encoding utf-8 -*-
# File name: Gradient_Descent.py
# Author: Muller Lee (X.C.Lee)
# Date: 2018/7/8

import numpy as np
import math
import matplotlib
import matplotlib.pyplot as plt
import random

'''
Global variables
'''
test_list=[[1,3],[2,4],[3,3],[5,6],[3,8],[2,5],[5,10],[6,8],[6,7],[7,6],[7,8],[10,11],[10,9],[9,9],[8,9],[2,1],[3,3],[5,8],[10,12],[12,11],[13,15],[11,13],[12,16]]
regre_var_1=random.randint(-5,5)
regre_var_2=random.randint(-5,5)

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
def f(x,y):
	for elem in test_list:
		diss.append((elem[0]*x-elem[1]+y)*(elem[0]*x-elem[1]+y)/(x*x+1))
	summ=0.0
	count=-1
	for rec in diss:
		summ=summ+rec
		count=count+1
	return summ/count
plt.ion()
n = 256
x = np.linspace(-5,5, n)
y = np.linspace(-5,5, n)
X,Y = np.meshgrid(x, y)
plt.contourf(X, Y,f(X,Y), 20, alpha=.75, cmap=plt.cm.hot)
C = plt.contour(X, Y,f(X,Y), 20, colors='black', linewidth=.5)
plt.clabel(C, inline=True, fontsize=10)
plt.xticks(())
plt.yticks(())
#plt.show()

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

#plt.ion()
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
	plt.scatter(regre_var_1,regre_var_2,s=10,edgecolors='None',c='white')
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

plt.savefig(('2D_GD.png'))
