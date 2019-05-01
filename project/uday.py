def function_tradewar(num1, num2, p1,p2,p3, p4,p1b,p2b,p3b,p4b,c1,c2):
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np
    player1 = []
    player2 = []
    iterator = []
    if(num1==100 and num2 ==100 ):
        for i  in range (1,101):
            player1.append(i*p1)
            player2.append(i*p1b)
    
    if(num2<num1):
        for i in range(1,num2):
            player1.append(i*p1)
            player2.append(i*p1b)
        for j in range (num2,num1):
            player1.append((num2-1)*p1 + p3+ (j-num2)*p3)
            player2.append((num2-1)*p1b + p3b+(j-num2)*p3b)
        for k in range(num1,101):
            player1.append((num2-1)*p1 + (num1-num2)*p3 +p4+ (k-num1)*p4)
            player2.append((num2-1)*p1b + (num1-num2)*p3b +p4b+ (k-num1)*p4b)
    if(num1<num2):
        for i in range (1,num1):
            player1.append(i*p1)
            player2.append(i*p1b)
    
        for j in range(num1,num2):
            player1.append((num1-1)*p1 + p2 + (j-num1)*p2)
            player2.append((num1-1)*p1b + p2b + (j-num1)*p2b)
        for k in range(num2,101):
            player1.append((num1-1)*p1 + (num2-num1)*p2 +p4+ (k-num2)*p4 )
            player2.append((num1-1)*p1b + (num2-num1)*p2b +p4b + (k-num2)*p4b)
    for i in range(1,101):
        iterator.append(i)
    plt.plot(iterator,player1,label = c1)
    plt.plot(iterator,player2,label = c2)
    plt.xlabel('Year')
    plt.ylabel('Payoffs(in billion USD)')
    plt.title('My Game')
    plt.legend()
    plt.show()

