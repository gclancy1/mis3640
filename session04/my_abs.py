def brian_abs(number):
    if isinstance(number, int):

        if number >= 0:
            return number
        else:
            return -number
    else:
        return 'I don\'t know'

# my_abs(10)
# my_abs(-10)
# my_abs(0)
# print(my_abs(-4.2))
