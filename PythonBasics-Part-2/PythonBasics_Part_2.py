#Задача 1. Напишите функцию без аргументов, которая выводит строку "Привет, Python!".

# def say_hello():   
#     print('Привет, Python!')

# print(type(say_helloo))   #<class 'function'>
# say_hello()              #Привет, Python!


## Задача 2. Напишите функцию, которая принимает имя пользователя и выводит приветствие.

from math import pi


def say_hello(name):
     print(f'Привет, {name}!')

# name = input("Введите имя: ")
# say_hello(name)     

# def say_hello2(name = "Aleks"):
#     print(f'Привет, {name}!')

# say_hello2()  # Привет, Aleks!   
''' New comment '''

# Задача 3. Напишите функцию, которая принимает два числа и возвращает их сумму.

# def add2(x,y):
#      return x + y

# z = add2(5,7)
# print(f'x + y = {z}')

# def summa3(x1, x2 = 0):
#   '''сумма двух чисел'''
#   global b
#   b = x1 + x2
#   return b
# b = 10
# print(b)        #10
# a = summa3(5)
# print(a)        #5
# print(b)        #5 !

# Задача 4. Создайте функцию, которая возвращает наибольшее из трёх чисел.

# def maxList(arr): 
#     arr.sort()
#     return arr[-1]

# def max3(a,b,c):
#   if a >= b and a >= c:
#     return a
#   elif b >= a and b >= c:
#     return b
#   else:
#     return c

# ls = [1,3,2]
# print(maxList(ls))   #3
# print(max3(3,2,1))   #3

# import math
# print(math.cos(3.14))
# print(math.cos(math.pi))

# Задача 5. Напишите лямбда-функцию для возведения числа в квадрат.

# sqrt = lambda x: x**2
# s = sqrt(5)
# print(s)       #25

# sm = lambda x,y: x+y
# print(sm(2,4))  #6

# Задача 6. Напишите функцию apply(func, x), которая принимает функцию и число, 
# применяет функцию к числу и возвращает результат. Пример:

# def apply(func,x):
#     res = func(x)
#     return res

# res = apply(sqrt, 5)
# print(res)   #25

# def apply2(func,x,y):
#     res = func(x,y)
#     return res

# res = apply2(sm, 2, 4)
# print(res)   #6

# apply(say_hello, 'Вася')


# Задача 7. С помощью map возведите список чисел [1, 2, 3, 4] в квадрат.
# def square(number):
#     return number ** 2

# numbers = [1, 2, 3, 4]

# # Apply the 'square' function to each number in the 'numbers' list
# squared_numbers_map = map(square, numbers)
# print(type(squared_numbers_map))

# # Convert the map object to a list to see the results
# squared_numbers_list = list(squared_numbers_map)
# print(squared_numbers_list)

# plus_one_map = map(lambda x:x+1, numbers)
# plus_one_list = list(plus_one_map)
# print(plus_one_list)

# Задача 8. С помощью filter оставьте только чётные числа из списка [5, 8, 11, 14].

# ls = [5, 8, 11, 14]

# def isEven(num):
#      return num % 2 == 0

# even_fl = filter(isEven, ls)
# print(list(even_fl))

# Задача 9. Используя reduce (из модуля functools), найдите произведение 
# всех чисел в списке [1, 2, 3, 4, 5].

# from functools import reduce 

# def multiplay(x,y):
#     return x * y

# ls = [1, 2, 3, 4, 5]
# s = reduce(multiplay, ls)
# print(s)   #120

# Задача 10. Напишите функцию, которая принимает список строк и возвращает список их длин с помощью map.

# ls = ['hello', 'bye', 'hola']

# def str_length(st):
#     return len(st)

# st_len_map = map(str_length, ls)
# print(list(st_len_map))

# OOP
# Задача 11. Создайте класс Dog, у которого есть атрибут name и метод bark(), выводящий "Гав-гав!".

# class Dog():
#     def __init__(self, name):
#         self.name = name

#     def bark(self):
#         print(f'{self.name}: Гав-гав-гав!')

# sharik = Dog('Шарик')
# print(type(sharik)) #<class '__main__.Dog'>
# print(sharik.name)  #Шарик
# sharik.bark()  #Шарик: Гав-гав-гав!
# sharik.name = "Матроскин"
# print(sharik.name)  #Матроскин

# sharik.bark = lambda :print('Мяу!')
# sharik.bark()  #Мяу!

# class Dog2():
#   def __init__(self, name):
#     self.name = name
#   def bark(self, voice = 'Гав-гав!'):
#     print(voice)
# sharik = Dog2('Шарик')
# print(sharik)
# print(type(sharik))

# sharik.bark("Мяу!")

# Задача 12. Создайте класс Rectangle, у которого есть методы для вычисления площади и периметра.

# class Rectangle():
#     def __init__(self, x, y):
#         self.x = self.y = 0

#         if x >= 0 and y >= 0:
#             self.x = x
#             self.y = y            

#     def square(self):
#         return self.x * self.y

#     def perim(self):
#         return (self.x + self.y) * 2
    
# rec = Rectangle(5, 10)
# print(rec.square())  #50
# print(rec.perim())   #30

# rec = Rectangle(5, -10)
# print(rec.square())  #0
# print(rec.perim())   #0

# Задача 13. Создайте класс Person и класс Student, 
# наследующийся от Person. Добавьте в Student метод study().

# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def birthday_pass(self):
#         return self.age + 1

# class Student(Person):
#     def __init__(self, name, age, subject):         
#         super().__init__(name, age)
#         self.subject = subject

#     def study(self):
#         print(f'{self.name} сидит за книжками по {self.subject}')

# st = Student('Alex', 62, "AI/ML")
# st.study()  #Alex сидит за книжками по AI/ML

# ps = Person('Petr', 40)
# age = ps.birthday_pass()
# print(ps.name, age) #Petr 41

#Задача 14. Реализуйте класс Car с приватным атрибутом __speed. 
#Добавьте методы для увеличения и уменьшения скорости.

# class Car():
   
#     def __init__(self):
#         self.__speed = 0 

#     def up_speed(self):
#         if self.__speed < 190:
#             self.__speed += 10
#             print(f"speeding +++ {self.__speed}")

#     def down_speed(self):
#         if self.__speed > 0:
#             self.__speed -= 10
#             print(f"breaking --- {self.__speed}")

# car = Car()

# car.up_speed()  #speeding +++ 10
# car.up_speed()  #speeding +++ 20
# car.up_speed()  #speeding +++ 30
# car.up_speed()  #speeding +++ 40

# car.down_speed()    #speeding --- 30
# car.down_speed()    #speeding --- 20

#Задача 15. Создайте класс MathUtils с методом класса pi() (возвращает число 3.14) и статическим методом add(a, b), 
#который возвращает сумму.

# class MathUtils():

#     # constr по умолчанию

#     @classmethod          # Class.method_name()
#     def pi(MathUtils, x): #pi(cls, x)
#         return 3.14 * 2

#     @staticmethod
#     def add(a, b):
#         return a + b

# mu = MathUtils()

# a = 6
# b = 8
# print(mu.add(a,b))
# print(MathUtils.add(a,b))

# print(mu.pi(2))
# print(MathUtils.pi(2))

#Задача 16. Создайте класс Vector, который описывает двумерный вектор с координатами x и y.

# Реализуйте магические методы:
# o str для красивого вывода вида (x, y)
# o add для сложения двух векторов
# o sub для вычитания
# o eq для проверки равенства векторов
# o lt и gt для сравнения длин векторов.
# Продемонстрируйте работу на примерах.

class Vector():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return (f'{self.x},{self.y}')

    def __add__(self, other):        
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):        
        return Vector(self.x - other.x, self.y - other.y)

    def __eq__(self, other):        
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):        
        return self.x < other.x and self.y < other.y

vc1 = Vector(3, 4) 
vc2 = Vector(5, 6) 

print(vc1)        #3,4
print(vc2)        #5,6
vc3 = vc1 + vc2

print(type(vc3))  #<class '__main__.Vector'>
print(vc3)        #8,10

vc4 = vc2 - vc1
print(vc4)        #2,2

print(vc1 == vc2) #false
print(vc1 == vc1) #true
print(vc1 < vc2)  #true