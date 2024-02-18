import random
print('enter any name to enter the game')
cust_name=input()
#usage of random import
ran_num=random.randint(0,10)
print('enter a number:')
cust_num=int(input())
guesses=1
while True:
#    guesses=+1
    if cust_num == ran_num:
        print('Your guess is correct!',cust_name)
        break
    else:
#        print('take another guess...')
#        cust_num=int(input())
        if cust_num<ran_num:
            print('guess higher')
            guesses=guesses+1
            cust_num=int(input())
        elif cust_num> ran_num:
            print('guess lower')
            guesses=guesses+1
            cust_num=int(input())
        continue
print('You took', guesses,'no. of guesses, to guess the number:', ran_num)