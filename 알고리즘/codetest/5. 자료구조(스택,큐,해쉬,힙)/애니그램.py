alphabet1 = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0,
            'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0,
            'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0,
            'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0,
            'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

alphabet2 = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0,
            'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0,
            'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0,
            'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0,
            'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
a = input()
a = a.lower()
b = input()
b = b.lower()

for x in a:
    alphabet1[x]+=1

for x in b:
    alphabet2[x]+=1

if alphabet1==alphabet2:
    print('YES')
else:
    print('NO')
