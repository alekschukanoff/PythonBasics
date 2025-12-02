#Задача 1. Напишите функцию без аргументов, которая выводит строку "Привет, Python!".

# def say_hello():   
#     print('Привет, Python!')

# print(type(say_helloo))   #<class 'function'>
# say_hello()              #Привет, Python!


## Задача 2. Напишите функцию, которая принимает имя пользователя и выводит приветствие.

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

sqrt = lambda x: x**2
s = sqrt(5)
print(s)       #25

sm = lambda x,y: x+y
print(sm(2,4))  #6

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