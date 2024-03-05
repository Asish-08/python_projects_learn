#need to check the continuous iteration of the loop

import random

def roll_dice():
    return random.randint(1, 6)

players = input('Enter the number of players: ')

if players.isdigit() and int(players) >= 2:
    players = int(players)
    players_score = [0 for _ in range(players)]
    max_score = 50

    while max(players_score) < max_score:
        for player in range(players):
            print('Now it is player', player + 1, "'s turn")
            print('Your total score is:', players_score[player])

            current_score = 0
            while True:
                choice = input('Do you want to roll (y/n)? ')
                if choice.lower() == 'n':
                    print("Player", player + 1, "'s turn is over. Their score is:", players_score[player])
                    break  # Move to the next iteration of the for loop, representing the next player's turn
                elif choice.lower() == 'y':
                    value = roll_dice()
                    if value == 1:
                        print('You rolled a 1!')
                        current_score = 0
                        break
                    else:
                        current_score += value
                        print('You rolled', value)
                        print('Current score for player', player + 1, 'is:', current_score)

            players_score[player] += current_score
            print('Total score of player', player + 1, 'is:', players_score[player])
            quit
            if max(players_score) >= max_score:
                quit  # Exit the game if a player reaches the max score

                
else:
    print("The number of players must be greater than or equal to 2 to play this game")

max_score = max(players_score)
player_won = players_score.index(max_score) + 1
print('Player', player_won, 'has the highest score of:', max_score)
