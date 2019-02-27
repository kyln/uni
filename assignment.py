# Week 4 Assignment --
# I think I did the assignment correctly,
# though I may not have understood it as well as I would have liked.
# Please let me know how I can improve!

# Implementing divisible function from textbook
def is_divisible(x, y):
    if x % y == 1:
        return True
    else:
        return False

# Creating exponent function
def is_power(base, power):
    result = 1
    for index in range(power):
        result = result * base
    return result

# Wrapping the assignment so you are not greeted with a bunch of lines
def expand():
    Y = str(input("Execute Assignment? (press enter)\n>>> "))
    if Y == Y:
        print("0.) 1^2 = " + str((is_power(1,2))) + " \n Is divisible by 1? " + str(is_divisible(1,2)) + "\n")
        print("1.) 3^3 = " + str((is_power(3,3))) + " \n Is divisible by 1? " + str(is_divisible(3,3)) + "\n")
        print("2.) 10^1 = " + str((is_power(10,1))) + " \n Is divisible by 1? " + str(is_divisible(10,1)) + "\n")
        print("3.) 1^1 = " + str((is_power(1,1))) + " \n Is divisible by 1? " + str(is_divisible(1,1)) + "\n")
        print("4.) 27^3 = " + str((is_power(27,3))) + " \n Is divisible by 1? " + str(is_divisible(27,3)) + "\n")
        print("5.) 10^2 = " + str((is_power(10,2))) + " \n Is divisible by 1? " + str(is_divisible(10,2)) + "\n")
        print("6.) 2^1 = " + str((is_power(2,1))) + " \n Is divisible by 1? " + str(is_divisible(2,1)) + "\n")
        print("7.) 1^10 = " + str((is_power(1,10))) + " \n Is divisible by 1? " + str(is_divisible(1,10)) + "\n")
        print("8.) 5^9 = " + str((is_power(5,9))) + " \n Is divisible by 1? " + str(is_divisible(5,9)) + "\n")
        print("9.) 5^1 = " + str((is_power(5,1))) + " \n Is divisible by 1? " + str(is_divisible(5,1)) + "\n")
    else:
        print("An error occurred.")

expand()