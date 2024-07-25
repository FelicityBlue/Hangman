import random

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

#Word bank of animals
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

def check_answer(player_guess, ans, guess ):
  
  for i in range(0, len(str(player_guess))):
    if i < len(ans):
      if player_guess[i] == ans[i]:
        guess[i] = ans[i]
    else:
      break

def main():
  ans = random.choice(words)
  error_count = 0
  
  guess = ["_"] * len(ans)

  while True:
    print(*guess, sep = " ")
    # Display hint
    print("HINT: Animals")
    
    # Display hangman
    print(HANGMANPICS[error_count])
    
    player_guess = input(str("Enter your guess: ")).lower()
    
    check_answer(player_guess, ans, guess)
    
    print(*guess, sep = " ")
    
    # Check win condition
    if error_count == 6:
      print("YOU LOST")
      break
    else:
      if "_" not in guess:
        print("YOU WON!")
        break
      else:
        error_count += 1
    
    
    
if __name__ == "__main__":
  main()