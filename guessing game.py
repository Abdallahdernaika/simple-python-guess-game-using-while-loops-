secret_number = 45
Guess_count = 0
Guess_limit =  3
while Guess_count <  Guess_limit:
    guess = int(input('guess: '))
    Guess_count+= 1
    if guess == secret_number:
        print('damnnnnn')
        break
else:
    print('you failed')
  
    
