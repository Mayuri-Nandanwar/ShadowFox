#Hangman: Implement the wordguessing game with visual progress and hints.

import random

#word list with hints
words_with_hints ={
    "python"   : "A popular programming language",
    "Java"     : "A widely-used programming language for building applications",
    "Algorithm": "A step-by-step procedure to solve a problem",
    "Database" : "A system used to store and manage data",
    "Compiler" : "A program that converts code into machine language",
    "Variable" : "A container for storing data values"
}

#hangman stages 
Stages = [
    """
     -----
     |   |
         |
         |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    --------
    """
]

#choose any word
word = random.choice(list(words_with_hints.keys()))
hint = words_with_hints[word]

guessed_letters = []
wrong_attempts = 0 
max_attempts = len(Stages) - 1

print("🎮 Welcome to Hangman!")
print("Hint:", hint)

while True:
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "__"
            
    print("\nWord :", display_word)
    print(Stages[wrong_attempts])
    
    #check winner
    if all(letter in guessed_letters for letter in word):
        print("🎉 Congratulations! You guessed the word:", word)
        break

    # Take input
    guess: str = input("Enter a letter: ")

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess not in word:
        wrong_attempts += 1
        print("Wrong guess!")

        if wrong_attempts == max_attempts:
            print(Stages[wrong_attempts])
            print("💀 Game Over! The word was:", word)
            break
    else:
        print("Correct guess!")
