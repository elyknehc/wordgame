import random

words = ["able", "belt", "bolt", "cast", "cash", "knot", "note", "near", "over", "salt", "wind"]

class Word:

    def __init__(self):
        self.word = random.choice(words)

class Game:

    # Constructor accepts a word object
    def __init__(self, word):
        self.word = word
        self.guesses = 5
        

    def handleGuess(self, guess):

        # Check if the guess is correct
        if guess == self.word.word:
            print("You got it! Amazing")
            return True
        else:
            self.giveUserHint(guess, self.word.word)
            print("Wrong guess! Try again: ")
            return False
    
    def giveUserHint(self, guess, word):

        hint = [0]*len(word)

        for i in range(len(word)):

            if guess[i] == word[i]:
                hint[i] = "1"
            elif guess[i] in word:
                hint[i] = "0"
            else: 
                hint[i] = "-"
        
        print(hint)
    
    def play(self):
        print("Welcome to Word Guess! You have " + str(self.guesses)  + " turns to guess the word")

        while self.guesses > 0:

            guess = input("Please enter your first guess:")

            while guess not in words:
                guess = input("That word is not in the list, please try again ")
            
            guess = guess.lower()

            if (self.handleGuess(guess)) == True:
                break
            else:
                self.guesses -= 1
        
        print("You're out of turns, game over!")


# Create a word object
word = Word()
game = Game(word)
game.play()