number = 10

print("I'm thinking of a number...")
guess = input("What number am I thinking of? ")

if int(guess) == number:
   print("Congratulations! You guessed the right number.")
else:
   while guess != number:
    guess = input(f"Sorry! The number you picked was incorrect. Try again or type 'q' to quit.  ")
    if str(guess) == 'q':
      print(f'The number you were trying to guess was {number}')
      break
    elif int(guess) == number:
        print("Congratulations! You guessed the right number.")
        break
    else:
        continue    
      
    