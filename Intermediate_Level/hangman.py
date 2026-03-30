#Hangman: Implement the wordguessing game with visual progress and hints.

import random

# words with hints
words = {
    "python": "A popular programming language",
    "java": "A widely used programming language",
    "algorithm": "A step-by-step way to solve a problem",
    "database": "Used to store and manage data",
    "compiler": "Converts code into machine language",
    "variable": "Used to store values"
}

# hangman stages
stages = [
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

# pick a random word
chosen_word = random.choice(list(words.keys()))
hint = words[chosen_word]

guessed = []
wrong = 0
max_wrong = len(stages) - 1

print("Welcome to Hangman!")
print("Hint:", hint)

# game loop
while True:
    display = ""

    for ch in chosen_word:
        if ch in guessed:
            display += ch + " "
        else:
            display += "_ "

    print("\nWord:", display)
    print(stages[wrong])

    # check if player won
    if all(ch in guessed for ch in chosen_word):
        print("Congratulations! You guessed the word:", chosen_word)
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed:
        print("You already tried that letter.")
        continue

    guessed.append(guess)

    if guess not in chosen_word:
        wrong += 1
        print("Wrong guess!")

        if wrong == max_wrong:
            print(stages[wrong])
            print("Game Over! The word was:", chosen_word)
            break
    else:
        print("Good guess!")