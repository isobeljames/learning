import random
from hm_words import words

word = random.choice(words)
reveal = list(len(word)*'_')
lives = 7
gameWon = False

while gameWon == False and lives > 0:
    print(reveal)
    guess = input("Guess a letter or an entire word:")
    guess = guess.upper()

    if guess == word:
        gameWon = True
    if len(guess) == 1 and guess in word:
        for i in range(0,len(word)):
            letter = word[i]
            if guess == letter:
                reveal[i] = guess
        if '_' not in reveal:
            gameWon = True
    else:
        lives -= 1

if gameWon:
    print("Well done, you guessed it!")
else:
    print(f"You failed, the word was {word}")

# checking this shows up now with my new email
