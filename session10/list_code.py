   1: >>> a = []
   2: >>> type(a)
list
   3: >>> len(a)
0
   4: >>> a = [10, 20, 30, 40]
   5: >>> b = ['spam', 2.0, 5, [10, 20]]
   6: >>> len(b)
4
   7: >>> len(b[0])
4
   8: >>> b[0]
'spam'
   9: >>> b[-1]
[10, 20]
  10: >>> b[3]
[10, 20]
  11: >>> len(b[3])
2
  12: >>> AFC_east = ['New England Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York Jets']
  13: >>> AFC_east
['New England Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York Jets']
  14: >>> print(AFC_east)
  15: >>> AFC_east[2] = 'New York Giants'
  16: >>> AFC_east
['New England Patriots', 'Buffalo Bills', 'New York Giants', 'New York Jets']
  17: >>> b
['spam', 2.0, 5, [10, 20]]
  18: >>> b[3]
[10, 20]
  19: >>> b[4]
  20: >>> b[3][2]
  21: >>> b
['spam', 2.0, 5, [10, 20]]
  22: >>> b[3][0]
10
  23: >>> b[3] = [10]
  24: >>> b
['spam', 2.0, 5, [10]]
  25: >>> b[3] = 10
  26: >>> type(b[3])
int
  27: >>> b
['spam', 2.0, 5, 10]
  28: >>> 'a'  in name
  29: >>> name = 'Brian'
  30: >>> 'a' in name
True
  31: >>> 'Buffalo Bills' in AFC_east
True
  32: >>> 'Miami Dolphins' in AFC_east
False
  33:
>>> L = [
...     ['Apple', 'Google', 'Microsoft'],
...     ['Java', 'Python', ['Ruby','On Rail'], 'PHP'],
...     ['Adam', 'Bart', 'Lisa']    
... ]
...
  34: >>> L[0][0]
'Apple'
  35: >>> L[0][9]
  36: >>> len(L)
3
  37: >>> L[2][2]
'Lisa'
  38: >>> L[1][2][1]
'On Rail'
  39: >>> L[1][2][1][2]
' '
  40: >>> name
'Brian'
  41:
>>> for whatever in name:
...     print(whatever)
...
  42:
>>> for whatever in AFC_east:
...     print(whatever)
...
  43:
>>> for letter in name:
...     print(letter)
...
  44:
>>> for team in AFC_east:
...     print(team)
...
  45:
>>> for team in AFC_east:
...     for letter in team:
...         print(letter)
...
  46: >>> numbers = [2019, 10, 8, 3, 43]
  47:
>>> for i in range(len(numbers)):
...     numbers[i] = numbers[i] * 2
...
  48: >>> numbers
[4038, 20, 16, 6, 86]
  49:
>>> for number in numbers:
...     print(number)
...
  50: >>> numbers = [2019, 10, 8, 3, 43]
  51:
>>> for number in numbers:
...     print(number)
...
  52:
>>> for number in numbers:
...     number = number * 2
...
  53: >>> numbers
[2019, 10, 8, 3, 43]
  54: >>> a
[10, 20, 30, 40]
  55: >>> b
['spam', 2.0, 5, 10]
  56: >>> b[2] = AFC_east
  57: >>> b
['spam',
 2.0,
 ['New England Patriots', 'Buffalo Bills', 'New York Giants', 'New York Jets'],
 10]
  58: >>> len(b)
4
  59: >>> a  = [1, 2, 3]
  60: >>> b = [4, 5, 6]
  61: >>> c = a + b
  62: >>> c
[1, 2, 3, 4, 5, 6]
  63: >>> import numpy as np
  64: >>> a = np.Arry([1, 2, 3])
  65: >>> a = np.Array([1, 2, 3])
  66: >>> [0] * 4
[0, 0, 0, 0]
  67: >>> ['Tom Brady', 'Bill Belichick']*3
['Tom Brady',
 'Bill Belichick',
 'Tom Brady',
 'Bill Belichick',
 'Tom Brady',
 'Bill Belichick']
  68: >>> t = ['a', 'b', 'c', 'd', 'e', 'f']
  69: >>> t[1:2]
['b']
  70: >>> t[1:3]
['b', 'c']
  71: >>> t[0:5]
['a', 'b', 'c', 'd', 'e']
  72: >>> t[0:4]
['a', 'b', 'c', 'd']
  73: >>> t[:4]
['a', 'b', 'c', 'd']
  74: >>> t[3:6]
['d', 'e', 'f']
  75: >>> t[3:]
['d', 'e', 'f']
  76: >>> t[::2]
['a', 'c', 'e']
  77: >>> t[:]
['a', 'b', 'c', 'd', 'e', 'f']
  78: >>> t[::-2]
['f', 'd', 'b']
  79: >>> t[::-1]
['f', 'e', 'd', 'c', 'b', 'a']
  80: >>> name[::-1]
'nairB'
  81: >>> t = ['a', 'b', 'c', 'd', 'e', 'f']
  82: >>> t[1:3] = ['x', 'y']
  83: >>> t
['a', 'x', 'y', 'd', 'e', 'f']
  84: >>> t[1:3] = ['Shaun', 'Jinna']
  85: >>> t
['a', 'Shaun', 'Jinna', 'd', 'e', 'f']
  86: >>> t[1:3] = ['Victoria']
  87: >>> t
['a', 'Victoria', 'd', 'e', 'f']
  88: >>> t[1:3] = 'Nico'
  89: >>> t
['a', 'N', 'i', 'c', 'o', 'e', 'f']
  90: >>> t = ['a', 'Victoria', 'd', 'e', 'f']
  91: >>> t[1] = 'Nico'
  92: >>> t
['a', 'Nico', 'd', 'e', 'f']
  93: >>> type(t[1:3])
list
  94: >>> type(t[1])
str
  95: >>> names = ['Nico', 'Myat', 'Carmen', 'Victoria']
  96: >>> names.append('Demi')
  97: >>> names
['Nico', 'Myat', 'Carmen', 'Victoria', 'Demi']
  98: >>> boys = ['Shaun', 'Brian', 'Krishna', 'Patrick']
  99: >>> names.reverse()
 100: >>> names
['Demi', 'Victoria', 'Carmen', 'Myat', 'Nico']
 101: >>> boys
['Shaun', 'Brian', 'Krishna', 'Patrick']
 102: >>> names.extend(boys)
 103: >>> names
['Demi',
 'Victoria',
 'Carmen',
 'Myat',
 'Nico',
 'Shaun',
 'Brian',
 'Krishna',
 'Patrick']
 104: >>> names = ['Nico', 'Myat', 'Carmen', 'Victoria']
 105: >>> names + boys
['Nico', 'Myat', 'Carmen', 'Victoria', 'Shaun', 'Brian', 'Krishna', 'Patrick']
 106: >>> names
['Nico', 'Myat', 'Carmen', 'Victoria']
 107: >>> names.append(boys)
 108: >>> names
['Nico',
 'Myat',
 'Carmen',
 'Victoria',
 ['Shaun', 'Brian', 'Krishna', 'Patrick']]
 109: >>> names = ['Nico', 'Myat', 'Carmen', 'Victoria']
 110: >>> names = names + boys
 111: >>> names
['Nico', 'Myat', 'Carmen', 'Victoria', 'Shaun', 'Brian', 'Krishna', 'Patrick']
 112: >>> 'jinna'.capitalize()
'Jinna'
 113: >>> t = [1, 2, 3]
 114: >>> sum(t)
6
 115: >>> names
['Nico', 'Myat', 'Carmen', 'Victoria', 'Shaun', 'Brian', 'Krishna', 'Patrick']
 116: >>> names.pop()
'Patrick'
 117: >>> names
['Nico', 'Myat', 'Carmen', 'Victoria', 'Shaun', 'Brian', 'Krishna']
 118: >>> names.pop(2)
'Carmen'
 119: >>> the_abandoned_name = names.pop(4)
 120: >>> the_abandoned_name
'Brian'
 121: >>> names
['Nico', 'Myat', 'Victoria', 'Shaun', 'Krishna']
 122: >>> names
['Nico', 'Myat', 'Victoria', 'Shaun', 'Krishna']
 123: >>> del names[3]
 124: >>> names
['Nico', 'Myat', 'Victoria', 'Krishna']
 125: >>> names.remove(1)
 126: >>> names.remove('Krishna')
 127: >>> names
['Nico', 'Myat', 'Victoria']
 128: >>> names.append('Nico')
 129: >>> names
['Nico', 'Myat', 'Victoria', 'Nico']
 130: >>> names.remove('Nico')
 131: >>> names
['Myat', 'Victoria', 'Nico']
 132: >>> names.append('Nico')
 133: >>> names
['Myat', 'Victoria', 'Nico', 'Nico']
 134: >>> names.remove('Nico')
 135: >>> name = 'Brian'
 136: >>> list(name)
['B', 'r', 'i', 'a', 'n']
 137: >>> letters = list(name)
 138: >>> letters
['B', 'r', 'i', 'a', 'n']
 139: >>> ''.join(letters)
'Brian'
 140: >>> ' '.join(letters)
'B r i a n'
 141: >>> '!!!'.join(letters)
'B!!!r!!!i!!!a!!!n'
 142: >>> team = 'New England Patriots'
 143: >>> team.split()
['New', 'England', 'Patriots']
 144: >>> words = team.split()
 145: >>> words
['New', 'England', 'Patriots']
 146: >>> ' '.join(words)
'New England Patriots'
 147: >>> ''.join(list('Brian'))
'Brian'
