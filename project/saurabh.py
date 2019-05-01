def saurabh1(a,b):
	import matplotlib.pyplot as plt
	import math
	noncoop_noncoop=[10,10]
	noncoop_coop=[5,15]
	coop_noncoop=[15,5]
	coop_coop=[20,20]
	one = int(a);
	two = int(b);
	total_one=1000
	total_two=1000
	total_three=1994
	payoff_one=[1000]
	payoff_two=[1000]
	payoff_three=[1994]
	if one > two:
		print("Is player1 more friendlier than hostile..?")
		kath=input()
		if kath == "no":
			one=math.floor(two/2)
        
	elif two>one:
		print("Is player2 more friendlier than hostile..?")
		rath=input()
		if rath == "no":
			two=math.floor(one/2)
        
	change_one=1000-one*10
	change_two=1000-two*10    
	index=[0]
	if one > two:
		i=0
		while total_two > change_two and total_one>20 and total_two >20 and total_three>40:        
			total_one-=20
			total_two-=20
			total_three-=40 
			payoff_one.append(total_one)
			payoff_two.append(total_two)
			payoff_three.append(total_three)
			i=i+1
    
		while total_one > change_one and total_one>15 and total_two>15 and total_three>20:
			total_one-=15
			total_two-=5
			total_three-=20 
			payoff_one.append(total_one)
			payoff_two.append(total_two)
			payoff_three.append(total_three)
			i=i+1
        
		while total_one > 10 and total_two > 10 and total_three>20:
			total_one-=10
			total_two-=10
			total_three-=20 
			payoff_one.append(total_one)
			payoff_two.append(total_two)
			payoff_three.append(total_three)
			i=i+1
        
	elif two >= one:
		i=0
		while total_one > change_one and total_one>20 and total_two>20 and total_three> 40:
			total_one-=20
			total_two-=20
			total_three-=40 
			payoff_one.append(total_one)
			payoff_two.append(total_two)
			payoff_three.append(total_three)
			i=i+1
        
		while total_two > change_two and total_one>15 and total_two>15 and total_three> 20:
			total_one-=5
			total_two-=15
			total_three-=20 
			payoff_one.append(total_one)
			payoff_two.append(total_two)
			payoff_three.append(total_three)
			i=i+1
        
		while total_one > 10 and total_two > 10 and total_three> 20:
			total_one-=10
			total_two-=10
			total_three-=20 
			payoff_one.append(total_one)
			payoff_two.append(total_two)
			payoff_three.append(total_three)
			i=i+1
	j = 0
	while j<i:
		j=j+1
		index.append(j)
	
	print('total value of payoff for 1st player is ',total_one)
	print('total value of payoff for 2nd player is ',total_two) 
	print('total value of payoff for 3rd player is ',total_three) 
   
	plt.plot(index, payoff_one, color='blue')
	plt.plot(index, payoff_two, color='red')
	plt.plot(index, payoff_three, color='black')
	plt.xlabel('Number of Trials')
	plt.ylabel('Payoff of players')
	plt.title('Plot showing payoffs of two players with trials')
	plt.show()            
	if total_one>total_two and total_one > total_three :
		return "\"Winner Winner Chicken Dinner\" - Player 1"
	elif total_two > total_one and total_two > total_three :    
		return "\"Winner Winner Chicken\" - Player 2"
	elif total_three > total_two and total_three > total_one :       
		return "\"Winner Winner Chicken Dinner\" - Player 3"
