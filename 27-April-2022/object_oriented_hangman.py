
import random
import sys
"""
How Hangman game Works
The Hangman program randomly selects a secret word from a list of secret words. The random module will provide this ability, so line 1 in program imports it.

The Game: Here, a random word (a fruit name) is picked up from our collection and the player gets limited chances to win the game.

When a letter in that word is guessed correctly, that letter position in the word is made visible. In this way, all letters of the word are to be guessed before all the chances are over.

For convenience, we have given length of word + 2 chances. For example, word to be guessed is mango, then user gets 5 + 2 = 7 chances, as mango is a five letter word.
"""


class RandomWord(object):
    """
    read the words from an outside file and return one of those words, randomly chosen
    """

    def __init__(self,filename):
        """
        By using the " self " keyword we can access the attributes and methods of the class in python. "__init__" is a reseved method in python classes. It is known as a constructor in object oriented concepts. This method called when an object is created from the class and it allow the class to initialize the attributes of a class.
        """

        with open(filename) as f:
            """
            The with statement creates a context manager that simplify the way files are opened and closed in Python programs. Without using the with statement a developer has to remember to close file handlers. This is automatically done by Python when using the with open…as pattern.


            """
            words_list = []
            """
            One convient data set is a list of all english words, accessible like so: from nltk.corpus import words word_list = words.words() #
            """

            for line in f:
                words_list.append(line.rstrip('\r\n'))
                """The append() method appends an element to the end of the list./
                The rstrip() method removes any trailing characters (characters at the end a string), space is the default trailing character to remove.
                """

            self.word = random.choice(words_list)
            """
            Taking random words from words text.
            """

    def display(self, guessed_letters_list):
        """
        Function to display the secret word with the letters that have been correctly guessed.
        """

        word_to_display = ""

        for letter in self.word:
            if letter in guessed_letters_list:
                word_to_display += " " + letter + " "

            else:
                word_to_display += " _ "

        print("This is your word so far:", word_to_display, "\n")
        print(f"The length of word is {len(self.word)}")
        return word_to_display


class Hangman(object):

    HANGMAN_PICS = ["", "O", "O-", "O-|", "O-|-", "O-|-<"]
    """
    we have taken  letter and operators for complete the design of hangman game 
    """


    def __init__(self):
        self.hangman = self.HANGMAN_PICS[0]

    def draw(self, num_incorrect_guesses_made):
        """
        Function to display the updated status of the hangman based on the number of incorrect guesses the player has made.
        """
        self.hangman = self.HANGMAN_PICS[num_incorrect_guesses_made]
        print(self.hangman)

        if num_incorrect_guesses_made == 5:
            """
            You have only doing five mistakes
            """
            print("You died!!")


class Game(object):

    WRONG_ANSWER_PUTDOWNS = ["NOPE!","Wow, you suck at hangman.","Your guy doesn'tstand a chance!","You're leaving him high and dry"]

    def __init__(self, filename):
        self.secret_word = RandomWord(filename)
        """
        Secret words imported random words
        """
        self.hangman = Hangman()
        self.num_incorrect_guesses_made = 0
        self.guessed_letters = []

    def play(self):
        """
        The main function that begins a new game of hangman.
        """

        print("\n*+*+*+*++*+*+*+*+*+*+*+* Welcome to Hangman! *+*+*+*+*+*+*+*+*+*+*+*+*+\n")

        option = input("Do you need the rules explained to you? Y/n: ")

        if option.lower() == "y":
            print("\nInstructions:\n" \
                  "A word will be chosen at random from the dictionary. Each turn you guess a letter.\n" \
                  "Every time you guess a letter that isn't in the word, your man gets closer to being hanged!\n" \
                  "When your hangman looks like this: O-|-< ...you're dead!\n" )

        print("Let's play hangman!\n")

        # Initialize the number of incorrect guesses made to 0
        while self.num_incorrect_guesses_made < 5:
            """
            With the while loop we can execute a set of statements as long as a condition is true.
            """
            if len(self.guessed_letters) == 0:
                self.secret_word.display(self.guessed_letters)

            letter_guess = input("Please guess a letter: ").lower()

            # Don't let them guess a non-alpha letter.
            while letter_guess.isalpha() is False:
                letter_guess = input("No special characters allowed! Only enter a letter, please: ").lower()

            # Once a valid letter is chosen, add it to guessed_letters
            if letter_guess not in self.guessed_letters:
                self.guessed_letters.append(letter_guess)

                if letter_guess not in self.secret_word.word:
                    print(random.choice(self.WRONG_ANSWER_PUTDOWNS))
                    self.num_incorrect_guesses_made += 1
                    self.hangman.draw(self.num_incorrect_guesses_made)

                else:
                    print("You chose wisely!\n")
                    self.hangman.draw(self.num_incorrect_guesses_made)

            else:
                print("You've already guessed the letter '%s', please choose a new letter." % letter_guess)

            current_word = self.secret_word.display(self.guessed_letters)

            print("These are the letters you've already guessed: ", self.guessed_letters)

            if "_" not in current_word:
                print("Congratulations! You've won!")
                sys.exit()

"""game = Game("words.txt")
game.play()"""