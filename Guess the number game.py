import random

x = input('Hello, what is your name? ')
print('so, ' +  x + ', I am thinking of a number between 1 and 10')

secret_number = random.randint(1,10)

for i in range(1,7):
    print('take a guess')
    
    guess = int(input())
    if guess < secret_number:
        print('Too Low')
    elif guess > secret_number:
        print('Too High')
    else:
        break
        
if guess == secret_number:
    print('good job, It took you ' + str(i) + ' guesses to guess my number')
else:
    print('Exceeded guess limits, My guess number was ' + str(secret_number))