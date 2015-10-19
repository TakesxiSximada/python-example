# -*- coding: utf-8 -*-
print(b'hello %b' % b'world')
print(b'x=%i y=%f' % (1, 2.5))
try:
    b'Hello %b!' % 'World'
except TypeError:
    print('raise type error.')
print(b'price: %a' % '10€')
