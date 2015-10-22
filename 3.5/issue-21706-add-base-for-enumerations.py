# -*- coding: utf-8 -*-
from enum import Enum


Animal = Enum('Animal', 'cat dog pig bird', start=10)
print(Animal.cat)
print(Animal.dog)
print(Animal.pig)
print(Animal.bird)
