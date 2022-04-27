import random
import sys

#for guessing the words we have taken random words list,
#import sys in python is loading the module named sys into the current namespace so that you can access the functions and anything else defined within the module using the module name. On of the most common items is the list of arguments created when the program was called. This is sys.argv 5.1K views View upvotes Answer requested by Jack Hill
#How Hangman game Works
# The Hangman program randomly selects a secret word from a list of secret words. The random module will provide this ability, so line 1 in program imports it.

# The Game: Here, a random word (a fruit name) is picked up from our collection and the player gets limited chances to win the game.

# When a letter in that word is guessed correctly, that letter position in the word is made visible. In this way, all letters of the word are to be guessed before all the chances are over.

# For convenience, we have given length of word + 2 chances. For example, word to be guessed is mango, then user gets 5 + 2 = 7 chances, as mango is a five letter word.




class Randomword(object):

#read the words from an outside file and return one of those words, randomly chosen


    def __init__(self,filename):
        
        #By using the " self " keyword we can access the attributes and methods of the class in python. "__init__" is a reseved method in python classes. It is known as a constructor in object oriented concepts. This method called when an object is created from the class and it allow the class to initialize the attributes of a class.
        

        with open(filename) as f:
        
        #The with statement creates a context manager that simplify the way files are opened and closed in Python programs. Without using the with statement a developer has to remember to close file handlers. This is automatically done by Python when using the with open…as pattern.
        

            words_list = []
            for line in f:
                if len(line) < 4:
                    words_list.append(line.rstrip('\r\n'))
                    #""The append() method appends an element to the end of the list./
                    #The rstrip() method removes any trailing characters (characters at the end a string), space is the default trailing character to remove.
            




class Hangman(object):
    HANGMAN_PICS = ["", "O", " O-", "O-|", "O-|-", "O-|-<"]
    # we have letter and operators for complete the design of hangman game to hang

    def __init__(self):
        self.hangman = self.HANGMAN_PICS[0]

    def draw(self,  num_incorrect_guesses_made):
        # function to display the updated status of the hangman based on the number of incorrect guesses the player has made.








class Game(object):
    WRONG_ANSWER_PUTDOWNS = ["NOPE!","WOW you suck at a hangman.","Your guy doesn'tstand a chance!","You are leaving him high and dry" ]

    def __init__(self,filename):
        self.secret_word = RandomWord(filename)
        
        #Secret words imported Rnadom words
        
        self.hangman = Hangman()
        self.num_incorrect_guesses_made = 0
        self.guessed_letters = []

    # for playing the game we add a new function "play"
    def play(self):


        #The main functions that begins a new game to hangman
        print("\n*************Welcome to Hangman************\n")

        option = input("Do you Need the rules explain to you? Y/n:")

        if option.lower() == "y":
            print("\nInstructions:\n" \
                "A word will be chosen at random from the dictionary.Each turn you guess a letter.\n" \
                " Every time you guess a letter that isn't in the word ")
            







