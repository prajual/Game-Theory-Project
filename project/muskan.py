def muskan1(a,b):
	import numpy as np
	import matplotlib.pyplot as plt
	import pandas as pd
	c =  [5.0 ,4.0,4.3,8.9,6.9,2.4,6.0,5.5,3.8,4.1]
	no = np.array(c)
	num1 = no[int(a)]
	num2 = no[int(b)]
	num1 = int(100 - (num1*100)/(num1 + num2))
	num2 = int(100 - (num2*100)/(num1 + num2))
	player1 = []
	player2 = []
	p1 = 20
	p11 = 30
	p2 = 40
	p22 = 10
	p3= 10
	p33 = 40
	p4 = 10
	p44 = 10
	if num1<num2:
		for i in range(1, num1):
			player1.append(i*p1)
			player2.append(i*p11)
		for j in range(1,num2-num1+1):
			player1.append((num1 - 1)*p1 + j*p2)
			player2.append((num1 - 1)*p11 + j*p22)
		for k in range(1,100-num2+2):
			player1.append((num1 - 1)*p1 + (num2-num1-1)*p2 + k*p4)  
			player2.append((num1 - 1)*p11 + (num2-num1-1)*p22 + k*p44)
	if num1>num2:
		for i in range(1, num2):
			player1.append(i*p1)
			player2.append(i*p11)
		for j in range(1,num1-num2+1):
			player1.append((num2 - 1)*p1 + j*p3)
			player2.append((num2 - 1)*p11 + j*p33)
		for k in range(1,100-num1+2):
			player1.append((num2 - 1)*p1 + (num1-num2-1)*p3 + k*p4)  
			player2.append((num2 - 1)*p11 + (num1-num2-1)*p33 + k*p44)
	time = []
	for i in range(1,101):
		time.append(i)
	payoff1=np.array(player1)
	payoff2=np.array(player2)
	plt.plot(time,payoff1,payoff2)
	plt.xlabel("Rounds")
	plt.ylabel("Payoffs")
	plt.title("Project")
	plt.show()

	return "Graphs for each of the player is shown"
