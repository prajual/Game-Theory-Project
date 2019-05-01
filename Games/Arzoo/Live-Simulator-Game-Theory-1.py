#!/usr/bin/env python
# coding: utf-8

# # This is a live Simulation that can typically be applied to any sort of 2 dimensional game. Just type in the roles of your character and see how does it affects the final profit of individual.
# 

# In[1]:


import random
import numpy as np
import matplotlib.pyplot as plt


# In[19]:


def givenash(game):
    validresponse,somethingnew,strategies=[],[],[]
    p1=[[game[0],game[2]],[game[1],game[3]]]
    p2=[[game[0],game[1]],[game[2],game[3]]]
    
    if max(p1[0][0][0],p1[0][1][0])==game[0][0]:
        taxp2=game[0]
    else:
        taxp2=game[2]
        
    if max(p1[1][0][0],p1[1][1][0])==game[1][0]:
        notaxp2=game[1]
    else:
        notaxp2=game[3]
            
    if game[0][1]==(max(p2[0][0][1],p2[0][1][1])):
        taxp1=game[0]
    else:
        taxp1==game[1]
        
    if (max(p2[1][0][1],p2[1][1][1])==game[2][1]):
        notaxp1=game[2]
    else:
        notaxp1=game[3]
    X=[taxp2,taxp1,notaxp2,notaxp1]
    for i in range(4):
        for j in range(i+1,4):
            #print(i,j,'\n')
            if X[i]==X[j]:
                validresponse.append(X[i])
    for i in validresponse:
        somethingnew.append(game.index(i))
    for i in somethingnew:
        if i==0:
            strategies.append([1,1])
        elif i==1:
            strategies.append([1,0])
        elif i==2:
            strategies.append([0,1])
        elif i==3:
            strategies.append([0,0])
    if(len(strategies)>1):
        return random.choice(strategies)
    else:
        return strategies[0]
    
    
#Enter your Game Parameters here.
    

    
# p1,p11 = (20,30)
# p2,p22 = (10,10)
# p3,p33 = (40,30)
# p4,p44 = (30,20)

# Payoffs=[[p1,p11],[p2,p22],[p3,p33],[p4,p44]]
# nash=givenash(Payoffs)
# print(nash)


# In[20]:


class behaviours:
    
    def behavefriendly(self):
        return 0
    
    def behaveangry(self,prevaction):
        if(prevaction==1):
            return 1
        else:
            return self.behavefriendly()
    
    
    def dontcare(self):
        return np.random.randint(0,2)
    
    
    def behaverational(self,Nashstrategies):
        if(self.name=='p1'):
            return Nashstrategies[0]
        else:
            return Nashstrategies[1]
        
    def behavefool(self,game):
        p1max=[i[0] for i in game[:]].index(max([i[0] for i in game[:]]))
        p2max=[i[1] for i in game[:]].index(max([i[1] for i in game[:]]))
        if self.name=='p1':
            if p1max==0 or p1max==1:
                return 1
            else:
                return 0
        else:
            if p2max==0 or p2max==2:
                return 1
            else: 
                return 0
            

class player(behaviours):
    
    def __init__(self,name,behaviour):
        self.name=name
        self.behaviour=behaviour
        self.properties=[]
        self.actions=[]
        self.earnings=0
        
    def act(self,prevaction,nashstrategies,game):
        if self.behaviour=='angry':
            return self.behaveangry(prevaction)
        elif self.behaviour=='friendly':
            return self.behavefriendly()
        elif self.behaviour=='random':
            return self.dontcare()
        elif self.behaviour=='rational':
            return self.behaverational(nashstrategies)
        elif self.behaviour=='fool':
            return self.behavefool(game)
          
    def myacts(self,x):
        self.actions.append(x)
        
        
    


# In[13]:


behaviour1=input("How do you want your First player to be like??")
behaviour2=input("How do you want your Second player to be like??")
p1=input("Enter your game prameters, p1 to p44")
p11=input()
p2=input()
p22=input()
p3=input()
p33=input()
p4=input()
p44=input()


# In[22]:


def fx(game,player1behave,player2behave):
    p1=player('p1',behaviour1)
    p2=player('p2',behaviour2)
    nash=givenash(game)
    n=100

    for i in range(0,n):
        if len(p1.actions)!=0:
            prevact1=p1.actions[-1]
        else: 
            prevact1=0

        p2.myacts((p2.act(prevact1,nash,Payoffs)))

    for i in range(n):
        if len(p2.actions)!=0:
            prevact2=p2.actions[-1]
        else: 
            prevact2=0
        p1.myacts((p1.act(prevact2,nash,Payoffs)))

    actionss=[[p1.actions[i],p2.actions[i]] for i in range(n)]

    for i in actionss:
        if i==[1,1]:
            p1.earnings=Payoffs[0][0]+p1.earnings
            p1.properties.append(p1.earnings)
            p2.earnings=Payoffs[0][1]+p2.earnings
            p2.properties.append(p2.earnings)
        elif i==[1,0]:
            p1.earnings=Payoffs[1][0]+p1.earnings
            p1.properties.append(p1.earnings)
            p2.earnings=Payoffs[1][1]+p2.earnings
            p2.properties.append(p2.earnings)
        elif i==[0,1]:
            p1.earnings=Payoffs[2][0]+p1.earnings
            p1.properties.append(p1.earnings)
            p2.earnings=Payoffs[2][1]+p2.earnings
            p2.properties.append(p2.earnings)
        elif i==[0,0]:
            p1.earnings=Payoffs[3][0]+p1.earnings
            p1.properties.append(p1.earnings)
            p2.earnings=Payoffs[3][1]+p2.earnings
            p2.properties.append(p2.earnings)

    # print((p1.properties),"\n\n\n",(p2.properties))  
    get_ipython().run_line_magic('matplotlib', 'inline')
    plt.plot(range(100),p1.properties,linestyle='solid', label="Player1")
    plt.plot(range(100),p2.properties,linestyle='solid',label="Player2")
    plt.plot(range(100),[p1.properties[-1]]*100,linestyle='--')
    plt.plot(range(100),100*[p2.properties[-1]],linestyle='--')
    plt.xlabel('No. of Iterations')
    plt.ylabel('The profit obtained by each player')
    plt.title('This is how Game goes')
    plt.legend()
    plt.show()

game=[[int(p1),int(p11)],[int(p2),int(p22)],[int(p3),int(p33)],[int(p4),int(p44)]]    
fx(game,behaviour1,behaviour2)


# In[ ]:




