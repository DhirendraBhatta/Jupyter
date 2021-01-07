#Assignment of Rock Paper Scissor Game by Dhirendra Bhatta
import random
comp = random.randint(1,3)
print("Computer's generated input is: ",comp)
user = int(input('Enter 1 for rock,2 for paper and 3 for scissor  '))
while user not in [1,2,3]:
    user = int(input('Enter 1 for rock,2 for paper and 3 for scissor  '))
if user == comp:
    print("Computer and User both entered the same value.Hence it's draw.")
elif user == 1 and comp == 2:
    print(' Paper covers the rock.So Computer wins.')
elif user == 2 and comp == 3:
    print(' Scissor cuts paper.So Computer wins.')
elif user == 3 and comp == 1:
    print(' Rock broke scissor.So Computer wins.')
elif comp == 1 and user == 2:
    print('Paper covers the rock.So User wins.')
elif comp == 2 and user == 3:
    print('Scissor cuts the paper.So User wins.')
elif comp == 3 and user == 1:
    print('Rock broke the scissor.So User wins.')
else:
    print('Thank you for playing the game rock paper scissor')
