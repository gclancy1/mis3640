def binary_search(my_list, find):
    left = 0
    right = len(my_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if find == my_list[mid]:
            return mid
        elif find < my_list[mid]:
            right = mid - 1
        else:
            left = mid + 1


if __name__ == "__main__":
    test_list = [1, 3, 5, 235425423, 23, 6, 0, -23, 6434]
    test_list.sort()

    print(binary_search(test_list, -23))
    print(binary_search(test_list, 0))
    print(binary_search(test_list, 235425423))
    print(binary_search(test_list, 30))

    # expected output
    # 0
    # 1
    # 8
    # None
