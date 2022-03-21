def hello(name='Jack'):
    print('The hello() function has been executed!')

    def greet():
        return'\t This is greet() func inside hello!'

    def welcome():
        return'\t This is welcome() inside hello'

    print("I am going to return a function!!")


    if name == 'Jack':
        return greet
    else:
        return welcome

my_new_func = hello('Jack')

print(my_new_func() )