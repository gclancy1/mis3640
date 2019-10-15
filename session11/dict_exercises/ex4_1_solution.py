def create_dict():
    """
    Create a dictionary of words from words.txt
    """
    d = dict()
    f = open("session09/words.txt")
    for line in f:
        word = line.strip()
        d[word] = 0
    return d

def check_in_dict(word, d):
    """
    Return True if the word is in dictionary, d
    """
    return word in d

if __name__ == "__main__":
    word_dict = create_dict()
    word_to_check = input('Enter a word:')
    if check_in_dict(word_to_check, word_dict):
        print('Yes')
