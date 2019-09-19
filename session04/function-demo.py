def print_lyrics():
    print("Hey Jude. Don't make it bad.")
    print("Take a sad song and make it better.")

# print_lyrics()

# print(type(print_lyrics))

def repeat_lyrics():
    print_lyrics()
    print('Na - na - na - na - na, na - na - na - na')
    print_lyrics()

# repeat_lyrics()

def print_twice(name):
    print(name)
    print(name)


# print_twice('Brian')
# print_twice('Hey, Jude')

# his_name = 'Brian'
# print_twice(his_name)
# print_twice(42)

def cat_twice(part1, part2):
    cat = part1 + part2
    print(cat)
    # print_twice(cat)


# cat_twice(100, 200)
# print(cat)

# cat_twice('100', '200')


def give_me_a_break():
    msg = 'break'
    return msg

# print(give_me_a_break())
# print_twice(give_me_a_break())

# whatever_function_throws_to_me = give_me_a_break()

# print(whatever_function_throws_to_me)

def give_me_a_break():
    str1 = 'break'    
    return str1
    
# print(give_me_a_break())


from my_abs import brian_abs

print(brian_abs('A'))

# def f1():
#     pass

