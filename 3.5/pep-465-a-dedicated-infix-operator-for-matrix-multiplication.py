# -*- coding: utf-8 -*-
import numpy

x = numpy.ones(3)
m = numpy.eye(3)

res = x @ m
print(res)
print(res == numpy.ones(3))
