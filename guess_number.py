number = 10

print("I'm thinking of a number...")
guess = input("What number am I thinking of? ")
guess_limit = 5
if int(guess) == number:
   print("Congratulations! You guessed the right number.")
else:
   while guess != number:
    if guess_limit == 1:
        print(f'Sorry, you have run out of guesses. The number you were trying to guess was {number}')
        break
    else:
        guess_limit -= 1
    if int(guess) > number:
            print(f'The number is lower than {guess}')
            guess = input(f'Sorry! The number is higher than {guess}. You have {guess_limit} guesses remaining. Try again or type ''q'' to quit. ')
    elif int(guess) < number:
           guess = input(f'Sorry! The number is higher than {guess}. You have {guess_limit} guesses remaining.Try again or type ''q'' to quit. ')
  
    
    if str(guess) == 'q':
      print(f'The number you were trying to guess was {number}')
      break
    elif int(guess) == number:
        print("Congratulations! You guessed the right number.")
        break
    else:
        continue    
      
    