def capitalize_all(t):
    result = []
    for word in t:
        result.append(word.capitalize()) 
    
    return result

names = ['nico', 'myat', 'carmen', 'victoria']

print(capitalize_all(names))


def only_upper(t):
    res = []
    for s in t:
        if s[0].isupper():
            res.append(s)
    return res


names = ['Jinna', 'SHAUN', 'JENNY', 'Brian', 'julie', 'shirley']

print(only_upper(names))