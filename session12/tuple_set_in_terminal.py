   1: name = 'Shaun'
   2: name[0] = 'T'
   3: t = 'a', 'b', 'c'
   4: type(t)
tuple
   5: t[0]
'a'
   6: t[-1]
'c'
   7: t[0] = 'z'
   8: t = tuple('Babson')
   9: t
('B', 'a', 'b', 's', 'o', 'n')
  10: t = tuple([1, 2, 3])
  11: t
(1, 2, 3)
  12: tel = '123-456-5432'
  13: tel.split('-')
['123', '456', '5432']
  14: tel.split('-')[-1]
'5432'
  15: a, b, local = tel.split('-')
  16: local
'5432'
  17: *a, local = tel.split('-')
  18: local
'5432'
  19: a
['123', '456']
  20: tel ='+1-123-345-6533'
  21: international, *_, local = tel.split('-')
  22: international
'+1'
  23: local
'6533'
  24: international, local = tel.split('-')
  25: a = 10
  26: b = 20
  27: a, b = b, a
  28: a
20
  29: b
10
  30: divmod(7, 3)
(2, 1)
  31:
def f():
    return 1, 2
  32: f()
(1, 2)
  33: temp, humidity = f()
  34: temp
1
  35: humidity
2
  36:
def sumall(*nums):
    return sum(nums)
  37: sumall(1, 2, 3, 4, 5)
15
  38: sumall(1, 2)
3
  39:
def multiply(*nums):
    result = 1
    for num in nums:
        result *=num
  40:
def multiply(*nums):
    result = 1
    for num in nums:
        result *=num
    return result
  41: multiply(1, 2, 3, 4, 5, 6)
720
  42: s = set('victoria')
  43: s
{'a', 'c', 'i', 'o', 'r', 't', 'v'}
  44: s={1, 2, 3}
  45: s
{1, 2, 3}
  46: s = set('victoria')
  47: s
{'a', 'c', 'i', 'o', 'r', 't', 'v'}
  48: s.add('e')
  49: s
{'a', 'c', 'e', 'i', 'o', 'r', 't', 'v'}
  50: s.add('e')
  51: s
{'a', 'c', 'e', 'i', 'o', 'r', 't', 'v'}
  52: s = {1, 2, 3}
  53: s1 = {1, 2, 3}
  54: s2 = {2, 3, 4}
  55: s1 & s2
{2, 3}
  56: s1 | s2
{1, 2, 3, 4}
  57: s1 + s2
  58: s1.difference(s2)
{1}
  59: word = 'bookkeeper'
  60: unique_letters =[]
  61:
for letter in word:
    if letter not in unique_letters:
        unique_letters.append(letter)
  62: unique_letters
['b', 'o', 'k', 'e', 'p', 'r']
  63: set(word)
{'b', 'e', 'k', 'o', 'p', 'r'}
  64: list(set(word))
['r', 'p', 'b', 'e', 'k', 'o']
  65: sorted(list(set(word)))
['b', 'e', 'k', 'o', 'p', 'r']
  66: # string and list
  67: name = 'victoria'
  68: name_l = list(name)
  69: name_l
['v', 'i', 'c', 't', 'o', 'r', 'i', 'a']
  70: ''.join(name_l)
'victoria'
  71: # string and dictionary
  72: name_d = dict()
  73:
for letter in name:
    name_d[letter] = name_d.get(letter, 0) + 1
  74: name_d
{'v': 1, 'i': 2, 'c': 1, 't': 1, 'o': 1, 'r': 1, 'a': 1}
  75: # string and tuple
  76: name_t = tuple(name)
  77: name_t
('v', 'i', 'c', 't', 'o', 'r', 'i', 'a')
  78: ''.join(name_t)
'victoria'
  79: # string and set
  80: name_s = set(name)
  81: name_s
{'a', 'c', 'i', 'o', 'r', 't', 'v'}
  82: # list and tuple
  83: name
'victoria'
  84: t = [1, 2, 3, 4, 5, 6, 7, 8]
  85: zip(name, t)
<zip at 0x23d63487508>
  86:
for pair in zip(name, t):
    print(pair)
  87: list(zip(name, t))
[('v', 1),
 ('i', 2),
 ('c', 3),
 ('t', 4),
 ('o', 5),
 ('r', 6),
 ('i', 7),
 ('a', 8)]
  88: # dictionary and tuples
  89: dict(zip(name, t))
{'v': 1, 'i': 7, 'c': 3, 't': 4, 'o': 5, 'r': 6, 'a': 8}
  90: name_d2 = dict(zip(name, t))
  91: name_d2.items()
dict_items([('v', 1), ('i', 7), ('c', 3), ('t', 4), ('o', 5), ('r', 6), ('a', 8)])