def payoff(state1,state2,i,player1,player2,u1,u2,u3,u4):
	import matplotlib.pyplot as plt
	import numpy as np
	import random
	if state1==1 and state2==1:
		player1.append(player1[i-1] + u1[0])
		player2.append(player2[i-1] + u1[1])
	elif state1==1 and state2==0:
		player1.append(player1[i-1]+u2[0])
		player2.append(player2[i-1]+u2[1])
	elif state1==0 and state2==1:
		player1.append(player1[i-1]+u3[0])
		player2.append(player2[i-1]+u3[1])
	else:
		player1.append(player1[i-1]+u4[0])
		player2.append(player2[i-1]+u4[1])

