import time

def display(lives):  #Displays the hangman figure based on how many lives are left.
    if lives == 6:
        print('''  +---+
  |   |
      |
      |
      |
      |
=========''')
    elif lives == 5:
        print('''  +---+
  |   |
  O   |
      |
      |
      |
=========''')    
    elif lives == 4:
        print('''  +---+
  |   |
  O   |
  |   |
      |
      |
=========''')
    elif lives == 3:
        print('''  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''')
    elif lives == 2:
        print('''  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''')    
    elif lives == 1:
        print('''  +---+
  |   |
  O   |
 /|\  |
   \  |
      |
=========''')
    else:
        print('''  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''')

def wordChoose():       #For the user to input the word to guess
    wordAccepted = False
    while wordAccepted == False:
        word = str(input('Please type in the word to be guessed: '))
        print("\n"*100)
        if word.isalpha():
            word = word.lower()
            print('Word accepeted! Thank you!') 
            return word
        else:
            print("That's not a word!")

def letterGuess():  #For the user to input their letter to guess.
    letter = str(input('Please type in the letter to guess: '))
    return letter

def main():
    gameOver = False
    guessedLetters = []
    lives = 6
    hiddenWord=[]
    word=list(wordChoose())
    for x in range(len(word)):
        hiddenWord.append('_')
    print('Hidden word: ' +' '.join(hiddenWord))
    while not gameOver:
        print(f'You have {lives} lives remaining!')
        letter=letterGuess()
        print('\n')
        if letter in guessedLetters:
            print("You've already guessed this!")
        elif letter not in word and len(letter)==1:
            lives -= 1
            guessedLetters.append(letter)
        elif letter in word and len(letter) ==1:
            for index, rightLetter in enumerate(word):
                if rightLetter == letter:
                    hiddenWord[index] = letter
            guessedLetters.append(letter)
        else:
            print('Incorrect input!')
        display(lives)
        print('Guessed letters: ' +' '.join(guessedLetters))
        print('Hidden word: ' +' '.join(hiddenWord))
        if lives<0 or hiddenWord == word:
            gameOver = True
    if lives<0:
        print('You lose!')
    else:
        print('Congrats!')
    time.sleep(5)

main()