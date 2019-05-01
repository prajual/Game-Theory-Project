def jay1(a,y1,z1,b,y2,z2):
    a = int(a)
    y1 = int(y1)
    z1 = int(z1)
    b = int(b)
    y2 = int(y2)
    z2 = int(z2)
    
    payoff = [[[10,10],[25,5]],[[5,25],[15,15]]]
    
    strategy = []
    for i in range(0,101):
        f = [1,1]
        strategy.append(f)
    
    rounds = 0
    
    x = min(a,b)
    
    player1 = 1
    player2 = 1
    
    fix = 0
    while rounds < 100 :
        if a >= 1 :
            player1 = 1
        else:
            player1 = 0
        if b >= 1 :
            player2 = 1
        else:
            player2 = 0
        if player1 == 1 and player2 == 1:
            strategy[rounds][0] = player1
            strategy[rounds][1] = player2
            a = a - 1
            b = b - 1
            if rounds == x:
                if a == x:
                    player1 = 0
                else:
                    player2 = 0
        if player1 == 0 and player2 == 1:
            strategy[rounds][0] = player1
            strategy[rounds][1] = player2
            b = b - 1
            if b <= 0:
                player2 = 0
            if y1 >= 1:
                y1 = y1 - 1
                a = a + 1
            if z2 >= 1:
                player2 = 0
                rounds = rounds + 1
                strategy[rounds][0] = player1
                strategy[rounds][1] = player2
                player1 = 0
                player2 = 0
                m = int((100-rounds)*z2/100)
                if rounds + m >= 101:
                    m = 100 - rounds
                for j in range(0,m):
                    rounds = rounds + 1
                    strategy[rounds][1] = player2
                    strategy[rounds][0] = player1
        if player1 == 1 and player2 == 0:
            strategy[rounds][0] = player1
            strategy[rounds][1] = player2
            a = a - 1
            if a <= 0:
                player1 = 0
            if y2 >= 1:
                y2 = y2 - 1
                b = b + 1
            if z1 >= 1:
                player1 = 0
                rounds = rounds + 1
                strategy[rounds][0] = player1
                strategy[rounds][1] = player2
                player1 = 0
                player2 = 0
                m = int((100-rounds)*z1/100)
                if rounds + m >= 101:
                    m = 100 - rounds
                for j in range(0,m):
                    rounds = rounds + 1
                    strategy[rounds][1] = player2
                    strategy[rounds][0] = player1
        if player1 == 0 and player2 == 0:
            strategy[rounds][1] = player2
            strategy[rounds][0] = player1
        rounds = rounds + 1
    
    payoff1 = []
    payoff2 = []
    for i in range(0,100):
        m = strategy[i][0]
        n = strategy[i][1]
        if m == 0 and n == 0:
            payoff1.append(payoff[0][0][0])
            payoff2.append(payoff[0][0][1])
        if m == 1 and n == 0:
            payoff1.append(payoff[1][0][0])
            payoff2.append(payoff[1][0][1])
        if m == 0 and n == 1:
            payoff1.append(payoff[0][1][0])
            payoff2.append(payoff[0][1][1])
        if m == 1 and n == 1:
            payoff1.append(payoff[1][1][0])
            payoff2.append(payoff[1][1][1])
        
    import matplotlib.pyplot as plt
    
    payoff3 = []
    for i in range(0,100):
        payoff3.append(15)
    s = 1
    
    while s < 100:
        payoff1[s] = payoff1[s-1] + payoff1[s]
        payoff2[s] = payoff2[s-1] + payoff2[s]
        payoff3[s] = payoff3[s-1] + payoff3[s]
        s = s +1
    
    plt.plot(payoff1,'red')
    plt.plot(payoff2,'blue')
    plt.plot(payoff3,'green')
    plt.title('iteration vs payoff')
    plt.xlabel('iteration')
    plt.ylabel('Payoff')
    plt.show()
    print("Player 1: ")
    print(payoff1[99])
    print("Player 2: ")
    print(payoff2[99])
    
    payoff1a = []
    payoff2a = []
    for j in range(0,5):   
        for i in range(0,100):
            m = strategy[i][0]
            n = strategy[i][1]
            if m == 0 and n == 0:
                payoff1a.append(payoff[0][0][0])
                payoff2a.append(payoff[0][0][1])
            if m == 1 and n == 0:
                payoff1a.append(payoff[1][0][0])
                payoff2a.append(payoff[1][0][1])
            if m == 0 and n == 1:
                payoff1a.append(payoff[0][1][0])
                payoff2a.append(payoff[0][1][1])
            if m == 1 and n == 1:
                payoff1a.append(payoff[1][1][0])
                payoff2a.append(payoff[1][1][1])
        
    import matplotlib.pyplot as plt
    
    payoff3a = []
    for i in range(0,500):
        payoff3a.append(15)
    s = 1
    
    while s < 500:
        payoff1a[s] = payoff1a[s-1] + payoff1a[s]
        payoff2a[s] = payoff2a[s-1] + payoff2a[s]
        payoff3a[s] = payoff3a[s-1] + payoff3a[s]
        s = s +1
        
    
    plt.plot(payoff1a,'red')
    plt.plot(payoff2a,'blue')
    plt.plot(payoff3a,'green')
    plt.title('iteration vs payoff')
    plt.xlabel('iteration')
    plt.ylabel('Payoff')
    plt.show()
    print("Player 1: ")
    print(payoff1a[499])
    print("Player 2: ")
    print(payoff2a[499])
