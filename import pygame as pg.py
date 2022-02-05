import random
rps2 = ['Rock', 'Paper', 'Scissors']
rps = random.choice(rps2)
spr = (input('Enter a choice Rock, Paper, or Scissors: '))
spr = str(spr)
print(rps)
if rps == 'Rock' and spr == 'Scissors':
    print('I win >:)')
elif rps == 'Scissors' and spr == 'Rock':
    print('You win :(')
elif rps == 'Paper' and spr == 'Scissors':
    print("You win :(")
elif rps == 'Paper' and spr == 'Rock':
    print('I win >:)')
elif rps == 'Rock' and spr == 'Paper':
    print('You win :(')
elif rps == 'Scissors' and spr == 'Paper':
    print('I win >:)')
elif rps == 'Rock' and spr == 'Rock':
    print('Tie, interesting')
elif rps == 'Paper' and spr == 'Paper':
    print('Tie, interesting')
elif rps == 'Scissors' and spr == 'Scissors':
    print('Tie, interesting')
else:
    print('Please enter on of the given options')
