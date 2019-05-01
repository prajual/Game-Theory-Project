def maisam1(a,b):
	import pandas as pd
	import numpy as np
	import matplotlib.pyplot as plt
	maxi = 100
	num1 = int(a)
	num2 = int(b)
	player1 = [0]
	player2 = [0]
	p1 = [30,30]
	p2 = [50,0]
	p3 = [0,50]
	p4 = [20,20]
	if (num1<num2):
    		for i in range(1,num1):
        		player1.append(player1[i-1]+p1[0])
        		player2.append(player2[i-1]+p1[1])
    		for i in range(num1,num2):
        		player1.append(player1[i-1]+p3[0])
       			player2.append(player2[i-1]+p3[1])
    		for i in range(num2,maxi+1) :  
        		player1.append(player1[i-1]+p4[0])
        		player2.append(player2[i-1]+p4[1])
	else:
    		for i in range(1,num2):
        		player1.append(player1[i-1]+p1[0])
        		player2.append(player2[i-1]+p1[1])
    		for i in range(num2,num1):
        		player1.append(player1[i-1]+p2[0])
        		player2.append(player2[i-1]+p2[1])
    		for i in range(num1,maxi+1):   
        		player1.append(player1[i-1]+p4[0])
        		player2.append(player2[i-1]+p4[1])
	time = []
	for i in range(1,102):
    		time.append(i)
	
	plt.plot(time, player1, label = "Player 1")
	plt.plot(player2, label = "Player 2")
	plt.xlabel("Rounds")
	plt.ylabel("Payoffs")
	plt.title('Repeated Games')
	plt.show()
	return "Payoff graph is shown for both the players"
