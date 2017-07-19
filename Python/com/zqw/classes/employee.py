#!/usr/bin/python
# -*- coding: UTF-8 -*-
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def displayemployee(self):
        print("name: %s" % self.name)
        print("age: %d" % self.age)

emp = Employee("zqw", 20)
emp.displayemployee()
print(Employee.__name__)

del emp