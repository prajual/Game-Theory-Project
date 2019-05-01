def aditya1(friendliness_1, imitation_1, vindictiveness_1, friendliness_2, imitation_2, vindictiveness_2):
    # taking parameters from user 1:: friendliness, imitation, vindictiveness.

    #friendliness_1 = input('As a baseline, with what probability (as a percentage of all rounds) will you cooperate, allowing free trade between your country and your opponents?\n')
    #imitation_1 = input('Once trade begins, your opponent policy could be unpredictable. With what probability (as a percentage of all rounds) will you abandon your baseline strategy to mimic their actions, responding to them in kind?')
    #vindictiveness_1 = input('If you are crossed by an unkind, defecting opponent who imposes tariffs on your goods, with what probability (as a percentage of the remaining rounds) do you hold a grudge, putting your other strategies aside to punish the other country by defecting yourself?')
    #
    #
    ## taking parameters from user 2:: friendliness, imitation, vindictiveness.
    #
    #friendliness_2 = input('As a baseline, how often (as a percentage of all rounds) will you cooperate, allowing free trade between your country and your opponent?')
    #imitation_2 = input('Once trade begins, your opponent policy could be unpredictable. How often (as a percentage of all rounds) will you abandon your baseline strategy to mimic their actions, responding to them in kind?')
    #vindictiveness_2 = input('If you are crossed by an unkind, defecting opponent who imposes tariffs on your goods, how long (as a percentage of the remaining rounds) do you hold a grudge, putting your other strategies aside to punish the other country by defecting yourself?')

    #friendliness_1 = input('friendliness: \n')
    #imitation_1 = input('imitation: \n')
    #vindictiveness_1 = input('vindictiveness: \n')
    #
    #friendliness_2 = input('friendliness: \n')
    #imitation_2 = input('imitation: \n')
    #vindictiveness_2 = input('vindictiveness: \n')
    import numpy as np
    import matplotlib as mpl
    import matplotlib.pyplot as plt

    #user1 response
    user1 = [0]
    #user2 response
    user2 = [0]

    flag1 = True
    flag2 = True

    friendliness_1 = int(friendliness_1)/100.00
    imitation_1 = int(imitation_1)/100.00
    vindictiveness_1 = int(vindictiveness_1)/100.00  

    friendliness_2 = int(friendliness_2)/100.00
    imitation_2 = int(imitation_2)/100.00
    vindictiveness_2 = int(vindictiveness_2)/100.00 

    #tendency to grudge for user 1..
    grudge_1 = 0
    #tendency to grudge for user 2..
    grudge_2 = 0

    #friendliness parameters---------------------------------
    y1 = 1-friendliness_1 #user1
    y2 = 1-friendliness_2 #user2
    #--------------------------------------------------------

    for iteration in range(100):
        #determining the next strategy for user 1
        if iteration > 0 and flag1 == True:
            if user2[iteration-1] == 0:
                flag1 = False

        #until user 2 don't defect
        if iteration == 0 or flag1 == True:
            if friendliness_1 >= y1:
                user1.append(1)
            elif friendliness_1 < y1 and iteration == 0:
                user1.append(0)
            
            else:
                if (friendliness_1 + friendliness_1*imitation_1) >= y1:
                    user1.append(1)
                else:
                    user1.append(0)
                    
            
                
        #if user 2 cooperate..
        elif user2[iteration-1] == 1:
            
            if grudge_1 >=0:
                prob_cooperation = ( pow(1-vindictiveness_1, grudge_1))*friendliness_1
            else:
                prob_cooperation = friendliness_1
                
            if prob_cooperation < y1:
                prob_cooperation = prob_cooperation*(1+imitation_1)
            
            
            if prob_cooperation >= y1:
                user1.append(1)
            else:
                user1.append(0)
                grudge_1 =  grudge_1 - 1
                
        #if user 2 defect..
        elif user2[iteration-1] == 0:
            grudge_1 = grudge_1 + 1
            
            if grudge_1 >=0:
                prob_cooperation = ( pow(1-vindictiveness_1, grudge_1))*friendliness_1*(1-imitation_1)
            else:
                prob_cooperation = friendliness_1*(1-imitation_1)
            
            
            if prob_cooperation >= y1:
                user1.append(1)
            else:
                user1.append(0)
                grudge_1 =  grudge_1 - 1
        
        #updates for game -----------------
        if friendliness_1 >= y1:
            friendliness_1 = friendliness_1 - 0.01
        else:
            friendliness_1 = friendliness_1 + 0.01
        #----------------------------------

        #---------------------------------------------------------------------------------End of loop for user1
        
        #determining the next strategy for user 2
        
        if iteration > 0:
            if user1[iteration-1] == 0:
                flag2 = False

        #until user 1 don't defect
        if iteration == 0 or flag2 == True:
            if friendliness_2 >= y2:
                user2.append(1)
            elif friendliness_2 < y2 and iteration == 0:
                user2.append(0)
            
            else:
                if (friendliness_2 + friendliness_2*imitation_2) >= y2:
                    user2.append(1)
                else:
                    user2.append(0)
                
        #if user 2 cooperate..
        elif user1[iteration-1] == 1:
            
            if grudge_2 >=0:
                prob_cooperation = ( pow(1-vindictiveness_2, grudge_2))*friendliness_2
            else:
                prob_cooperation = friendliness_2
                
            if prob_cooperation < y2:
                prob_cooperation = prob_cooperation*(1+imitation_2)
            
            
            if prob_cooperation >= y2:
                user2.append(1)
            else:
                user2.append(0)
                grudge_2 =  grudge_2 - 1
                
        #if user 2 defect..
        elif user1[iteration-1] == 0:
            grudge_2 = grudge_2 + 1
            
            if grudge_2 >=0:
                prob_cooperation = ( pow(1-vindictiveness_2, grudge_2))*friendliness_2*(1-imitation_2)
            else:
                prob_cooperation = friendliness_2*(1-imitation_2)
            
            
            if prob_cooperation >= y2:
                user2.append(1)
            else:
                user2.append(0)
                grudge_2 =  grudge_2 - 1

        #updates for game -----------------
        if friendliness_2 >= y2:
            friendliness_2 = friendliness_2 - 0.01
        else:
            friendliness_2 = friendliness_2 + 0.01
        #----------------------------------
        #--------------------------------------------------------------------------------End of loop for user2
    #---------------------------------------------------end of loop for determining the strategies for players


    #calculating the net profit generated by the players
    payoff_1 = (15, 5, 25, 10)
    payoff_2 = (15, 25, 5, 10)

    payoff_array1 = []
    payoff_array2 = []

    sum1 = 0
    sum2 = 0

    #profit generated by player 1

    for iteration in range(101):
        if user1[iteration] == 1 and user2[iteration] == 1:
            payoff_array1.append(sum1 + payoff_1[0])
            payoff_array2.append(sum2 + payoff_2[0])
            
            sum1 = sum1 + payoff_1[0]
            sum2 = sum2 + payoff_2[0]
            
        elif user1[iteration] == 1 and user2[iteration] == 0:
            payoff_array1.append(sum1 + payoff_1[1])
            payoff_array2.append(sum2 + payoff_2[1])
            
            sum1 = sum1 + payoff_1[1]
            sum2 = sum2 + payoff_2[1]
        
        elif user1[iteration] == 0 and user2[iteration] == 1:
            payoff_array1.append(sum1 + payoff_1[2])
            payoff_array2.append(sum2 + payoff_2[2])
            
            sum1 = sum1 + payoff_1[2]
            sum2 = sum2 + payoff_2[2]
        
        elif user1[iteration] == 0 and user2[iteration] == 0:
            payoff_array1.append(sum1 + payoff_1[3])
            payoff_array2.append(sum2 + payoff_2[3])
            
            sum1 = sum1 + payoff_1[3]
            sum2 = sum2 + payoff_2[3]

    #plotting--------------------------------------------
    A = list(range(1,102,1))


    plt.plot(A, payoff_array1)
    plt.plot(A, payoff_array2)

    plt.xlim(0,100)
    plt.ylim(0,2500)

    plt.xlabel('turns')
    plt.ylabel('profit earns')
    plt.show()

    #---------------------------------------------------
           
