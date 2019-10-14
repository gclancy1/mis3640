def get_data(aTuple):
    nums = ()
    words = ()
    for t in aTuple:
        nums = nums + (t[0],)
        if t[1] not in words:
            words = words + (t[1],)
    min_nums = min(nums)
    max_nums = max(nums)
    num_unique_words = len(words)
    return min_nums, max_nums, num_unique_words


small, large, words = get_data(((0, 'Greg'),
                                (10, 'Victoria'),
                                (15, 'David'),
                                (2019, 'Greg'),
                                (20, 'Victoria')))
