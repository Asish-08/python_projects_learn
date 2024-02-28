#took the story from chatGPT
print("**Story: The Quest in Hogwarts**") 
print("In the magical world of Hogwarts, there lies a mysterious challenge hidden within the castle's depths.")
print("It is said that only the bravest witches and wizards can uncover its secrets.")
print("Now, a young student embarks on a quest to prove their magical prowess and unravel the mysteries hidden within the ancient walls of Hogwarts.")
print('\n')

name = input("Type in your name, wizard: ")

print(name, ", your journey starts at the entrance of Hogwarts School of Witchcraft and Wizardry.")
if name =='harry':
   print('')
   print('***LORD VOLDEMORT SENDS HIS REGARDS***')
   print('')
print("")

# Initialize variables
lives = 3
visited = 0

print('Choose a chamber among three')

while visited < 3 and lives > 0:
    chamber = input("Chamber of Enchanted Armor / Chamber of Bewitched Statues / Chamber of Mystical Creatures: ")

    if chamber == 'chamber of enchanted armor':
        print('')
        print("There is a Dementor protecting the chamber!!!")
        print("Use one of the spells to counter attack the Dementor!!!")
        print('')
        spell = input("ExuroDraconis / Expecto patronum / Depulso: ").lower()
        if spell == 'expecto patronum':
            print("You've defeated the Dementor, wizard!!")
        else:
            print("You couldn't overcome the fear of the Dementor. You lost,", name)
            lives -= 1
            print('You have', lives, 'lives left.')
        visited += 1

    elif chamber == 'chamber of bewitched statues':
        print('')
        print("There is a Stone Sentinel protecting the chamber!!!")
        print("Use one of the spells to counter attack the Stone Sentinel !!!")
        print('')
        spell = input("ExuroDraconis / Expecto patronum / Depulso: ").lower()
        if spell == 'depulso':
            print("You've defeated the Stone Sentinel, wizard!!")
        else:
            print("The Stone Sentinel crushed you wizard. You lost,", name)
            lives -= 1
            print('You have', lives, 'lives left.')
        visited += 1

    elif chamber == 'chamber of mystical creatures':
        print('')
        print("There is a Basilisk protecting the chamber!!!")
        print("Use one of the spells to counter attack the Basilisk !!!")
        print('')
        spell = input("ExuroDraconis / Expecto patronum / Depulso: ").lower()
        if spell == 'exurodraconis':
            print("You've defeated the Basilisk, wizard!!")
        else:
            print("The Basilisk ate you wizard. You lost,", name)
            lives -= 1
            print('You have', lives, 'lives left.')
        visited += 1

    else:
        print('Enter a valid input')

print('')
if visited >= 3:
    print("Congratulations, wizard! You have successfully explored all three chambers of Hogwarts.")
else:
    print("Oh no, wizard! You have lost all your lives. Better luck next time!")

print("Thanks for playing!")
