def jay1(a,b):
	a = int(a)
	b = int(b)
	player1def = [1,0]
	player1cop = [5,3]
	player2def = [1,0]
	player2cop = [5,3]

	payoff = [[[1,1],[5,0]],[[0,5],[3,3]]]

	num = 100
	payoff1 = []
	payoff2 = []

	x = min(a,b)

	for i in range(1,x):
		payoff1.append(payoff[1][1][0])
		payoff2.append(payoff[1][1][1])

	if(a == x):
		for i in range(a,b):
			payoff1.append(payoff[0][1][0])
			payoff2.append(payoff[0][1][1])
		for i in range(b,num):
			payoff1.append(payoff[0][0][0])
			payoff2.append(payoff[0][0][1])

	if(b == x):
		for i in range(b,a):
			payoff1.append(payoff[1][0][0])
			payoff2.append(payoff[1][0][1])
		for i in range(a,num):
			payoff1.append(payoff[0][0][0])
			payoff2.append(payoff[0][0][1])

	import matplotlib.pyplot as plt
	for i in range(1,num-1):
		payoff1[i] = payoff1[i-1] + payoff1[i]
		payoff2[i] = payoff2[i-1] + payoff2[i]
    
	plt.plot(payoff1,'red')
	plt.plot(payoff2,'blue')
	plt.title('iteration vs payoff')
	plt.xlabel('iteration')
	plt.ylabel('Payoff')
	plt.show()
	return "Payoff graph is shown for both the players"
