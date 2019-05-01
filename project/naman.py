def naman1(a,b,c,d,e,f):
	import matplotlib.pyplot as plt
	import numpy as np
	import random
	from .naman1 import biasedflip
	from .naman2 import payoff
	player1 = [0]
	player2 = [0]
	friend1 = int(a);
	punish1 = int(b);
	strict1 = int(c);
	friend2 = int(d);
	punish2 = int(e);
	strict2 = int(f);
	u1 = [25, 25]
	u2 = [5, 60]
	u3 = [60, 5]
	u4 = [15, 15]

	state1 = 1
	state2 = 1

	for i in range(1, 100+1):
		if state2==1:
			p1 = friend1
		else:
			p1 = (((100-strict1)*friend1) + (strict1*(100-punish1)))/100
		if state1==1:
			p2 = friend2
		else:
			p2 = (((100-strict2)*friend2) + (strict2*(100-punish2)))/100    
		if biasedflip(p1):
			state1 = 1
		else:
			state1 = 0
		if biasedflip(p2):
			state2 = 1
		else:
			state2 = 0
		payoff(state1,state2,i,player1,player2,u1,u2,u3,u4)
	    
	time = []
	maxi = [0]
	for i in range(0, 100+1):
		time.append(i)
	for i in range(1, 100+1):
	    maxi.append(maxi[i-1]+25)

	payoff1 = np.array(player1)
	payoff2 = np.array(player2)
	maximum = np.array(maxi)
	plt.plot(time, payoff1, label = "Country 1")
	plt.plot(payoff2, label = "Country 2")
	plt.plot(maximum, label = "Free Trade")
	plt.xlabel("Rounds")
	plt.ylabel("Payoffs (in Billion Dollars)")
	plt.legend()
	plt.axis([0, 100, 0, 60*100])
	plt.show()
