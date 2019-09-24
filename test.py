def compare(varA, varB):
    if isinstance(varA, str):
        print("string involved")
        varA = 2

    if isinstance(varB, str):
        print("string involved")
        varB = 3

    if varA > varB:
        print("bigger")
    elif varA == varB:
        print("equal")
    else:
        print("smaller")

a = 'hello'
b = 3
c = 5

compare(a, b)
compare(b, c)