# def add(n1, n2):
#     print(n1+n2)
# add(10, 20)

# number1 = 10
# number2 = input("Please provide a number ")
# add(number1, int(number2))

# try:
#     result = 10+10
# except:
#     print("Hey it looks like you arent adding correctly.")
# else:
#     print("Add went well.")
#     print(result)

# try:
#     f = open("testfile","r")
#     f.write("Write a test line")
# except OSError:
#     print("All other exceptions.")
# finally:
#     print("I always run.")


def ask_for_int():
    while True:
        try:
            result = int(input("Please provide number. "))
        except:
            print("Whoops, that is not a number.")
            continue
        else:
            print("Yes, thank you")
            break
        finally:
            print("End of try/except/finally.")
            print("I will always run at the end.")
        
ask_for_int()
