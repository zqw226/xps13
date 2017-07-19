#!/usr/bin/python
# -*- coding: UTF-8 -*-
class Person:
    population = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('Initializing %s' % self.name)
        Person.population += 1

    def sayhi(self):
        print('hi，My name is %s.' % self.name)
        print('Er，My age is %d.' % self.age)

    def howmany(self):
        if Person.population == 1:
            print('I am the current population .')
        else:
            print('We have  %d persons here ' % Person.population)


swaroop = Person('Swaroop', 20)
swaroop.sayhi()
swaroop.howmany()

kalam = Person('Abdul kalam',27)
kalam.sayhi()
kalam.howmany()

swaroop.sayhi()
swaroop.howmany()