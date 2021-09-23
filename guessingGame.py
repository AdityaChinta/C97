import random
print('Number Guessing Game')
number=random.randint(1,5)
chances=0
print('Guess a number between 1 and 5')
while chances <5:
    guess=int(input('Enter your guess:-'))
    if guess==number:
        print('Congratulations,YOU HAVE WON!')
        break
    elif guess<number:
        print('Your guess was too low.',guess)
    else:
        print('Your guess was too high.',guess)
    chances+=1

if not chances<5:
    print('You lose,the number is: ',number)
