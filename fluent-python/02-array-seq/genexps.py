symbols = '$¢£¥€¤'

x = tuple(ord(symbol) for symbol in symbols)

print(x)

print(type(x))

import array

y = array.array('i', (ord(symbol) for symbol in symbols))

print(y)

print(type(y))