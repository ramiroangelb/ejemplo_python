
import random
HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''', '''
  +---+
 [O   |
 /|\  |
 / \  |
     ===''', '''
  +---+
 [O]  |
 /|\  |
 / \  |
     ===''']
words = {'Colors':'red orange yellow green blue indigo violet white black brown'.split(),
'Shapes':'square triangle rectangle circle ellipse rhombus trapazoid chevron pentagon hexagon septagon octogon'.split(),
'Fruits':'apple orange lemon lime pear watermelon grape grapefruit cherry banana cantalope mango strawberry tomato'.split(),
'Animals':'bat bear beaver cat cougar crab deer dog donkey duck eagle fish frog goat leech lion lizard monkey moose mouse otter owl panda python rabbit rat shark sheep skunk squid tiger turkey turtle weasel whale wolf wombat zebra'.split()}

hints = {'Colors' : 'roses are...ºcolor or fruit?ºuse it when drawing the sunºviolets are...ºfrom the India?ºI call it purple, you call it...ºthe color of the newspaperºthe color of Dark Themeºwood is...'.split("º"),
'Shapes' : '...Gardenºthree angles? how?ºrect an angle?ºPi cornersºEllie shapeºa bus making noiseºits a trap!ºits a chevie!ºUS securityºhexadecimal? thats crazy!ºseven wagons!ºeight wagons!'.split("º"),
'Fruits' : 'its redºits... I dont want to spoil it!ºits yellowºits greenºdissa...ºa melon in what?ºthey did surgery on a...ºthey did surgery on a... FRUITºHarry Styles best songºterracota pieºsing in spanish!ºlets go man!ºNo plastic straws!ºits red... ALL red'.split("º"),
'Animals' : ''.split("it flies!ºit sleeps!ºwhere?ºthey dont like usºa big cat!º...is gone!ºbeer?ºwoof woof!ºim not dumb!ºcuack cuackºI saw too much Vikingsºlives in the oceanºits green and jumpsºmeeeeehºleche?ºRAWRºits a dinosaurºlives in the treesºmouse?ºother what?ºbig eyesºJAPAN!ºthis languageºcarrots!ºits a plague!ºlives in the ocean and BITESºmeeeeeh... again!ºit stinksºink in minecraft!ºlion with stripesºits a country right?ºPowerShellºwe sealºBiggest mammal in the worldºAwoooooh!ºwom! It flies!ºMORE STRIPES!")
}

def getRandomWord(wordDict,hintDict): #Obtener palabra aleatoria
    ''' This function returns a random string from the passed dictionary of lists of strings, and the key also.'''
    
    # First, randomly select a key from the dictionary:
    wordKey = random.choice(list(wordDict.keys()))

    # Second, randomly select a word from the key's list in the dictionary:
    wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)
    
    # Asigna la pista correcta
    wordHint = hintDict[wordKey][wordIndex]

    return [wordDict[wordKey][wordIndex], wordKey,wordHint]

def displayBoard(missedLetters, correctLetters, secretWord): #Mostrar tablero
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): # replace blanks with correctly guessed letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: # show the secret word with spaces in between each letter
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed): #Obtener letra adivinada
    # Returns the letter the player entered. This function makes sure the player entered a single letter, and not something else.
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

def playAgain(): #Volver a jugar
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


print('H A N G M A N')

difficulty = 'X'
while difficulty not in 'EMH':
  print('Enter difficulty: E - Easy, M - Medium, H - Hard')
  difficulty = input().upper()
if difficulty == 'M':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
if difficulty == 'H':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
    del HANGMAN_PICS[5]
    del HANGMAN_PICS[3]

missedLetters = ''
correctLetters = ''
hintForWord = ''
secretWord, secretSet, hintForWord = getRandomWord(words,hints)
gameIsDone = False

while True:
    print('The secret word is in the set: ' + secretSet)
    print('Hint: ', hintForWord)
    displayBoard(missedLetters, correctLetters, secretWord)

    # Let the player type in a letter.
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Check if the player has won
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The secret word is "' + secretWord + '"! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # Check if player has guessed too many times and lost.
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True

    # Ask the player if they want to play again (but only if the game is done).
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord, secretSet, hintForWord = getRandomWord(words,hints)
        else:
            break