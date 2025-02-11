import random

words = ["able", "belt", "bolt", "cast", "cash", "knot", "note", "near", "over", "salt", "wind"]

class Word:

    def __init__(self):
        self.word = random.choice(words)

class Game:

    # Constructor accepts a word object
    def __init__(self, word):
        self.word = word
        

    def handleGuess(self, guess):

        # Check if the guess is correct
        if guess == self.word.word:
            print("Correct!")
        else:
            print("Incorrect!")

# Create a word object
word = Word()
game = Game(word)

print(game.handleGuess("able"))