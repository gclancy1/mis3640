def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


def print_hist(h):
    for c in h:
        print(c, h[c])


with open("session11/she_loves_you.txt") as f:
    lyrics = f.read().split()
    print(lyrics)

beatles = histogram(lyrics)
print_hist(beatles)
