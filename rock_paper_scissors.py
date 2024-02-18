#need to create a prog that makes the computer to chhose from random on rock apaper and scissor and ask the user to type 
# in their choice of action and count the no of wins and losses he weigh
 
import random
actions=['rock','paper','scissors','quit']
cust_score=0
comp_score=0


while True:
    cust_action=input(("type in your choice of action rock, paper, scissors, quit:")).lower()
    comp_action=actions[random.randint(0,2)]
    
    if cust_action=='rock' and comp_action=='scissors':
        cust_score+=1
        print('\n')
        print('you won!')
        print("computer's action is:", comp_action)
        continue
    elif cust_action=='paper' and comp_action=='rock':
        cust_score+=1
        print('\n')
        print('you won!')
        print("computer's action is:", comp_action)
        continue
    elif cust_action=='scissors' and comp_action=='paper':
        cust_score+=1
        print('\n')
        print('you won!')
        print("computer's action is:", comp_action)
        continue
    if cust_action=='quit':
        print('')
        print('###########')
        print('Your score is:', cust_score)
        print('Computer score is:', comp_score)
        print('Total no of tries:', cust_score+comp_score)
        print('###########')
        print('')
        
        quit() # have to make sure to keep the quit always after the print statements.
        
    else:
        comp_score+=1
        print('\n')
        print('computer won this time')
        print("computer's action is:", comp_action)
        continue