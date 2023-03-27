# @some_decorator
# def simple_func():
#     #do simple stuff
#     # return something
#     pass

# def func():
#     return 1

# def hello():
#     return "Hello!"

# greet = hello
# # print(greet())
# #returns "Hello!"

# del hello

# print(greet())




def hello(name ="Damien"):
    print("The hello() function has been executed!")
    
    def greet():
        return '\t This is the greet function inside hello!'
    
    def welcome():
        return '\t This is welcome, inside hello!'
    
    print("I am going to return a function")
    
    if name == "Damien":
        return greet()
    else:
        return welcome




# my_new_func = hello('Damien')
# print(my_new_func)

# my_newer_func = hello("Christine")
# print(my_newer_func())

# def cool():
    
#     def supercool():
#         return "I am very cool"
    
#     return supercool

# some_func = cool()

# print(some_func())




# def hello():
#     return "Hi Damien!"

# def other(some_def_func):
#     print("Other code runs here!")
#     print(some_def_func())
    
# other(hello)




def new_decorator(original_func):
    
    def wrap_func():
        
        print("Some extra code, before original statement")
        
        original_func() 
        
        print("Some extra code, after the original function")
        
    return wrap_func

def func_needs_decorator():
    print("I want to be decorated")
    
decorated_function = new_decorator(func_needs_decorator)

# print(decorated_function())

@new_decorator
def func_needs_decorator():
    print("I want to be decorated")
    
print(func_needs_decorator())