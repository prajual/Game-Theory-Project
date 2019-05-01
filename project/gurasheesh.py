def gurasheesh1(a,b,c,d):
    import numpy as np
    import matplotlib.pyplot as plt
    pay_1 = []
    pay_2 = []
    p1=75
    p2=100
    p3=25
    p4=50
    i=1
    iterations=100
    coop_1= int(a)
    vind_1= int(b)
    coop_2= int(c)
    vind_2= int(d)
    
    
    num1= ((coop_1+ (100- vind_1))/200)*iterations
    num2= ((coop_2+ (100- vind_2))/200)*iterations
    
    
    
    if num1>=num2:
    	while i<num2:
    		pay_1.append(i*p1)
    		pay_2.append(i*p1)
    		i+=1
    	while i==num2:
    		pay_1.append(num2*p1 + (i-num2)*p3)
    		pay_2.append(num2*p1 + (i-num2)*p2)
    		i+=1
    	while i<=iterations:
    		pay_1.append(num2*p1 + (num1-num2)*p3 + (i-num1)*p4)
    		pay_2.append(num2*p1 + (num1-num2)*p2 + (i-num1)*p4)
    		i+=1
    
    if num2>=num1:
    	while i<num1:
    		pay_1.append(i*p1)
    		pay_2.append(i*p1)
    		i+=1
    	while i==num1:
    		pay_1.append(num1*p1 + (i-num1)*p2)	
    		pay_2.append(num1*p1 + (i-num1)*p3)
    		i+=1
    	while i<=iterations:
    		pay_1.append(num1*p1 + (num2-num1)*p2 + (i-num2)*p4)
    		pay_2.append(num1*p1 + (num2-num1)*p3 + (i-num2)*p4)
    		i+=1
    a=np.arange(0,100)
    
    plt.plot(a, pay_1, label = "player_1")
    plt.plot(a, pay_2, label = "player_2")
    
    plt.xlabel('No. of iterations')
    plt.ylabel('Payoff')
    plt.title('Project_ Game_theory')
    plt.show()

