def new_decorator(original_func):
    def wrap_func():

        print('Some extra code,before the original function')

        original_func()

        print('Some extra code,after the original function')

    return wrap_func

def func_needs_decorator():
    print("Want this code is decorated!!")

func_needs_decorator()