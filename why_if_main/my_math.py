def square(x):
    return x * x


def app():
    n = int(input("enter:"))
    print("In my_math: square of {} is {}.".format(n, square(n)))


if __name__ == '__main__':
    app()
