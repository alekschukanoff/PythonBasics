# Задача 1. Переменные и типы данных
# Создайте три переменные: строку, число и число с плавающей точкой. Выведите их на экран.
# Подсказка: используйте функцию print().
a = 'stroka'
b = 5
c = 2.67

# print(a, type(a))
# print(b, type(b))
# print(c, type(c))

# # Задача 2. Напишите функцию, которая принимает имя пользователя и выводит приветствие.
# name = input('Введите имя: ')
# age = input('Введите возраст: ')
# #print(type(name), type(age))
# print(f'Привет {name}, тебе {age} лет!')
# print(f'Привет {name}, тебе будет {int(age) + 1} лет в следующем году!')


# Задача 3. Списки Создайте список из 5 любых чисел. Выведите первый и последний элементы. 
# Подсказка: доступ к элементам через индексы list[0] и list[-1].

# ls = ['а', 0, 1.3 ]
# print(type(ls)) #<class 'list'>
# print(ls)

# list = [1, 2, 3, 4, 5]
# print(list[0], list[-2], list[-1])

# s = list[1:4] #<class 'list'>
# print(type(s))
# print(s)      #[2, 3, 4]

# s = list[:4] 
# print(s)      #[1, 2, 3, 4]

# s = list[3:] 
# print(s)      #[4, 5]

# s = list[0:5:2] 
# print(s)      #[1, 3, 5]

# s = list[-1:-6:-1] #[5, 4, 3, 2, 1]
# print(s) 

# s = 'abcde'
# print(type(s))  #str
# s2 = s[-1:-6:-1] #edcba
# print(s2) 

# Задача 4. Кортежи Создайте кортеж с 4 фруктами. Выведите второй элемент. 
# Подсказка: кортеж похож на список, но его нельзя изменять.

# tp = ('apple', 'banana', 'orange', 'mango')
# print(type(tp))
# print(tp)  # ('apple', 'banana', 'orange', 'mango')
# fr = tp[1] # str
# print(type(fr))
# print(fr) # banana

# # tp[1] = 'grape'  error!

# ls = list(tp) # cast to list
# print(type(ls)) #<class 'list'>
# print(ls) #['apple', 'banana', 'orange', 'mango']

# ls[1] = 'grape'  
# print(ls)  #['apple', 'grape', 'orange', 'mango']


# Задача 5. Словари Создайте словарь с ключами 'имя', 'возраст', 'город'. 
# Заполните своими данными и выведите 'город'. Подсказка: доступ к значению — dict['ключ'].

st_ls = ['Василий', 20, 'Москва']
print(type(st_ls))
st_dict = {'Имя':'Василий', 'Возраст': 20, 'Город': 'Москва'}
print(type(st_dict))
