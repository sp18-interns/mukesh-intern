word = input("Please Enter a word: ")
word = str(word)
rvs=word[::-1]
print(rvs)
if word == rvs:
    print("The word is palindrome")
else:
    print("The word is not palindrome")
