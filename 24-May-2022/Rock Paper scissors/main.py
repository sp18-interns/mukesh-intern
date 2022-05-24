import sys

user1 = input("what is your name?")
user2 = input("And your name?")
user1_answer = input("%s, Now play, you want to choose rock, paper or scissors?" % user1)
user2_answer = input("%s,Now play,do you want to choose rock, paper or scissors?" % user2)


def compare(u1,u2):
    if u1 == u2:
        return "It's a tie!"
    elif u1 == 'rock':
        if u2 == 'scissors':
            return"Rock wins!"
        else:
            return"paper wins!"
    elif u1 == 'scissors':
        if u2 == 'paper':
            return"scissors win!"
        else:
            return"Rock win"
    elif u1 == 'paper':
        if u2 == 'rock':
            return"paper win"
        else:
            return"scissors win!"
    else:
        return"Invalid input! You  words are out  of this  rock, paper or scissors, try again."
        sys.exit()

print(compare(user1_answer,user2_answer))



