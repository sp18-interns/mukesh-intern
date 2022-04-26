import random
import sys

#for guessing the words we have taken random words list,
#import sys in python is loading the module named sys into the current namespace so that you can access the functions and anything else defined within the module using the module name. On of the most common items is the list of arguments created when the program was called. This is sys.argv 5.1K views View upvotes Answer requested by Jack Hill

class Randomword(object):

#read the words from an outside file and return one of those words, randomly chosen


    def __init__(self,filename):
        
        #By using the " self " keyword we can access the attributes and methods of the class in python. "__init__" is a reseved method in python classes. It is known as a constructor in object oriented concepts. This method called when an object is created from the class and it allow the class to initialize the attributes of a class.
        

        with open(filename) as f:
        
        #The with statement creates a context manager that simplify the way files are opened and closed in Python programs. Without using the with statement a developer has to remember to close file handlers. This is automatically done by Python when using the with open…as pattern.
        

            words_list = []:
            for line in f:
                words_list.append(line.rstrip('\r\n'))
                #""The append() method appends an element to the end of the list./
                #The rstrip() method removes any trailing characters (characters at the end a string), space is the default trailing character to remove.
            




class Hangman(object):
    HANGMAN_PICS = ["", "O", " O-", "O-|", "O-|-", "O-|-<"]







class Game(object):






