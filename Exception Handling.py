# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
"""
try
except
finally
else
"""
"""
print("Start") 

a = 5
b = 0

try:
    print(a/b)
except ZeroDivisionError:
    print("Handle Zero divide error")
""" 
"""
a = 5
b = 2


try:
    c = a/b
    print(c)
except:
    print("Handle Zero divide error")
"""

"""
a = 5
b = 2

try:
    c = a/b
    print(c)
except ZeroDivisionError:
    print("Handle Zero divide error")
except TypeError:
    print("Type Error Occured")
else:
    print(c*2)
"""

"""
a = 5
b = 2

try:
    c = a/b
    print(c)
except ZeroDivisionError:
    pass
"""

"""
a = 5
b = 0
d = []
try:
    c = a/b
    e = d[5]
except Exception as f:
    print("Handle Error ="+str(f))
else:
    print(c)
"""
"""
a = 5
b = 5
d = []
try:
    c = a/b
    e = d[5]
except ZeroDivisionError:
    print("Handle Zero Division Error")
except Exception as f:
    print("Handle Error = "+str(f))
else:
    print(c)
finally:
    print("Finally print this message")
print("Finish")

"""
"""
class Student():
    def __init__(self,name,age):
        if age > 80 or age < 16:
            raise Exception("Age out of range")
        self.name = name
        self.age = age

print("Before")
st = Student("Hello",19)
print (st.name)
print (st.age)
"""

class Student():
    def __init__(self,name,age):
        if age > 80 or age < 16:
            raise Exception("Age out of range")
        self.name = name
        self.age = age

class StudentAgeException(Exception):
    pass

print("Before")
try:
    st = Student("Hello",9)
except StudentAgeException as e:
    print("StudentAgeException = "+str(e))
else:
    print(st.age)

print("After")