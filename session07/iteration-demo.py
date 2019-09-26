# exercise 1

# result = 0

# for i in range(2, 1001, 2):
#     result += i
#     # result = result + i

# print(result)


# what is sum of squares of integers from 1 to 100(inclusive)?

# result = 0

# for i in range(1, 1001):
#     result += i * i
#     # result = result + i

# print(result)


def countdown(n):
    import time

    while n > 0:
        print(n)
        n -= 1
        time.sleep(1)
    print("Blastoff!")


# countdown(5)

# iteration = 0
# count = 0
# while iteration < 5:
#     # the variable 'letter' in the loop stands for every
#     # character, including spaces and commas!
#     for letter in "hello, world":
#         count += 1
#     print("Iteration " + str(iteration) + "; count is: " + str(count))
#     iteration += 1


# iteration = 0
# while iteration < 5:
#     count = 0
#     for letter in "hello, world":
#         count += 1
#     print("Iteration " + str(iteration) + "; count is: " + str(count))
#     iteration += 1

# iteration = 0
# while iteration < 5:
#     count = 0
#     for letter in "hello, world":
#         count += 1
#         if count % 2 == 0:
#             break
#     print("Iteration " + str(iteration) + "; count is: " + str(count))
#     iteration += 1


# exercise 2-2

# result = 0
# i = 1

# while i <= 10:
#     print(f"Before adding square of {i} , sum is {result}.")
#     result += i*i
#     i += 1
#     # i = i + 1
#     print(f"after adding, sum becomes {result}, and i becomes {i}.")
#     print()

# print(result)

#3 using for loop
# result = 0

# for i in range(1, 11):
#     result += i*i
#     print(f'after adding square of {i}, sum becomes {result}.')
#     print()





# while True:
#     line = input('> ')
#     if line.lower() == 'done':
#         break
#     print(line)

# print('Done!')



# mysum = 1
# for i in range(1, 5, 2):
#     # mysum += i    
#     mysum = mysum + i
#     if mysum == 2:
#         break
# print(mysum)