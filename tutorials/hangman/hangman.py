import random, hm_images, os
from hm_words import words

word = random.choice(words)
reveal = list(len(word)*'_')
lives = 7
gameWon = False

def check_letter(letter, word):
    global reveal # using the global reveal as this is what you're changing
    for i in range(0,len(word)):
        letter = word[i]
        if guess == letter:
            reveal[i] = guess
    if '_' not in reveal:
        return True
    else:
        return False

def status():
    os.system('clear')
    print(hm_images.hangman[7-lives]) # which image to access
    print("\n")
    print(' '.join([str(e) for e in reveal]))
    print("You have", lives, "lives remaining")
    print("\n")

while gameWon == False and lives > 0:
    status()
    guess = input("Guess a letter or an entire word:")
    guess = guess.upper()

    if guess == word:
        gameWon = True
        reveal = word
    if len(guess) == 1 and guess in word:
        gameWon = check_letter(guess, word)
    else:
        lives -= 1
    status() # so it prints out the word at the end

if gameWon:
    print("WELL DONE, YOU GUESSED IT!")
else:
    print(f"YOU FAILED, THE WORD WAS {word}")
