# age = int(input("Please enter your age:"))

# print(f"Your age is {age}.")

# if age >= 18:
#     print("You are an adult.")
# elif age>= 10:
#     print("You are a teenager.")
# else:
#     print("You are a kid.")

# if age >= 6:
#     print("teenager")
# elif age >= 18:
#     print("adult")
# else:
#     print("kid")

# from bmi_calculator import calculate_bmi

# weight = input('Enter your weight: ')
# height = input('Enter your height: ')
# weight = float(weight)
# height = float(height)

# calculate_bmi(weight, height)


def compare(varA, varB):
    if isinstance(varA, str) or isinstance(varB, str):
        print("string involved")
    else:
        if varA > varB:
            print("bigger")
        elif varA == varB:
            print("equal")
        else:
            print("smaller")


a = "hello"
b = 3
c = 5

# compare(a, b)
# compare(b, c)


def diff21(n):
    """
    Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.
    """
    if n <= 21:
        return abs(n - 21)
    else:
        return abs(n - 21) * 2


# print(diff21(19))  # expecting 2
# print(diff21(10))  # expecting 11
# print(diff21(21))  # expecting 0


def countdown(n):
    import time
    time.sleep(1)
    
    if n <= 0:
        print("Blastoff")
    else:
        print(n)
        countdown(n - 1)

countdown(5)


