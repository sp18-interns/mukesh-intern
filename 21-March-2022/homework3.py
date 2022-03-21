def ask():

    waiting =  True
    while waiting:
        try:
            n = int(input("Enter a number"))
        except:
            print("Please try again! \n")
            continue
        else:
            waiting = False

    print("Your number squared is:")
    print(n**2)

ask()

   