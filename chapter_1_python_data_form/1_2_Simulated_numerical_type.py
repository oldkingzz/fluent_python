# @Time: 2024-03-20 22:37
# @Author: DORK3333
# Email: lywangzesen2003@163.com
# @File: 1_2_Simulated_numerical_type.py
# Software: PyCharm
# Copyright (c) 2024 DORK3333. All rights reserved.
# Version: 1.0.0
# Description:

from math import hypot

class Vector:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Vector(%r, %r)" % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)