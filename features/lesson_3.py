# #TUPLES
#
# tuple_1 = () # создаем пустой тюпл
# print(type(tuple_1))# какой тип
# tuple_2 =(1, 2, 3, 4, 5)# создаем не пустой тюпл
# print(tuple_2)
# tuple_3 = tuple(range(5, 11))#создаем не пустой тюпл с длиной от 5 до 11
# print(tuple_3)
# tuple_4 = tuple('Pythont')# создаем стринг тюпл
# print(tuple_4)
# print(tuple_3 + tuple_4)# конкотинация
# print(tuple_3 * 3)# выводим на печать 3 раза
# print(tuple_4[5])# выводим на печать 5 символ
# print(tuple_4[1:5])# выводим на печать символы с 1 по 5
# print(tuple_4[1:5:2])# выводим на печать символы с 1 по 5 с шагом 2
# print(len(tuple_2))# cчитаем кол-во элементов в нашем тюпле
# print(max(tuple_2))# макс знач
# print(min(tuple_2))# мин знач
# print(min(tuple_4))# мин знач стринг
# print(max(tuple_4))# мах знач стринг
# print(tuple_4.index('t'))# индех знака
# print(tuple_4.count('t'))# считает сколько раз 't' встречается в заданном слове

# tuple_1 = tuple('pythont')
# list_1 = list('pythont')
# # tuple_1[0] = 'P'
# list_1[0] = 'P'
# print(tuple_1)
# print(list_1)

#Dictionary

# a = dict(one=1,two=2,three=3)
# print(a)
# b = {'one': 1, 'two': 2, 'three': 3}
# print(b)
# print(b['one'])
# d = dict([(2,'two'),(1,'one'),(3,'three')])
# print(d)
# d[2] = 'three'# заменить значение переменной 2 на three
# del d[3]#удалить three
# print(d)
# print(2 in d)# есть ли в дик d 2 >>>True
# print(3 not in d)# нет ли в дик d 3 >>>True

# b['five'] = 5#добавляем новое значение


# items = b.items()
# new_items = list(items)
# new_items.append(('four',4))#добавляем новое значение
# b = dict(new_items)

# print(b.keys())# показывает ключи
# print(b.values())# показывает значение

#result = b.pop('two')# удаляет элемент 2
# result = b.popitem()# удаляет последний элемент
# b.update(red = 1, blue = 2)
# b.update([('two',10)])# меняет значение ключа "two" на 10
# print(b)
# d=b.copy()
# print(d)
# print( b == d )

# d = dict.fromkeys(a)
# print(b.get('two'))

###############FUNCTION###############################
# number_1 = 20
# number_2 = 10
# def our_first_function(number):
#        print(number / 2)
#
# our_first_function(number_1)
# our_first_function(number_2)
# our_first_function(number_1 * number_2)

# def our_first_function(number):
#     return number / 2
#
# number_1 = 20
# number_2 = 10
# result_1 = our_first_function(number_1)
# print(result_1)
# result_2 = our_first_function(number_2)
# print(result_2)

######ADVENS
# def our_first_function(number = 50, number_1 = 80):
#     print(number_1)
#     return number / 2
#
# print(our_first_function(90,60))

# def our_first_function(number_1, number_2, *args):
#     print(args)
#     return number_1 / number_2
#
# print(our_first_function(90,60,30,10))


# def our_first_function(number_1, number_2=99, *args,**kwargs):
#     print(args)
#     print(kwargs)
#     return number_1 / number_2
#
# print(our_first_function(30,100,84,10,number_3=90,number_4=60))


####################Home work########################
#1. Create a tuple containing the names of five countries and display the whole tuple. Ask the user to enter one of the
# countries that have been shown to them and then display the index number (i.e. position in the list)
# of that item in the tuple.
# tuple_1 = ('Ukraine','USA','Brazil','Germany','Franse')
# cuntry = input('Enter one of cuntry: ')
# print(tuple_1.index(cuntry))
# print(tuple_1)
#
# #2. Add to the previous program to ask the user to enter a number and display the country in that position.
# number_1 = int(input('Enter number of cuntry: '))
# print(tuple_1[number_1])


#3. Write a Python script to add a key to a dictionary.
# dic_1 = { 3:'Kiev',4:'Dnepr'}
# dic_1[1] = 'Sarasota'
# print(dic_1)
# items = dic_1.items()
# new_items = list(items)
# new_items.append((2, 'Odessa'))
# dic_1 = dict(new_items)
# print(dic_1)
#
# # Sample Dictionary : {0: 10, 1: 20}
# # Expected Result : {0: 10, 1: 20, 2: 30}
# dic_2 = {0: 10, 1: 20}
# dic_2[2]=30
# print(dic_2)
#
#
# #3. Write a Python program to iterate over dictionaries using for loops.
# for x in dic_1:
#     if dic_1[x] == 'Odessa':
#         print(dic_1[x] + " is my hometown")
#     else:
#         print(dic_1[x] + ' is beautiful, but not my home')
#
#
# #4. Write a Python script to merge two Python dictionaries.
#
# dic_3 = dict(dic_1 | dic_2)
# print(dic_3)
#


#5. Write a Python program to remove duplicates from the Dictionary.

# test_dict = {'gfg': 10, 'is': 15, 'best': 20, 'for': 10, 'geeks': 20}
#
# # printing original dictionary
# print("The original dictionary is : " + str(test_dict))
#
# # Remove duplicate values in dictionary
# # Using dictionary comprehension
# temp = {val: key for key, val in test_dict.items()}
# res = {val: key for key, val in temp.items()}
#
# # printing result
# print("The dictionary after values removal : " + str(res))


# eg_dic={'gfg': 10, 'is': 15, 'best': 20, 'for': 10, 'geeks': 20}
# print("The original dictionary is:",eg_dic)
# temp=[]
# res={}
# for key,val in eg_dic.items():
#     if val not in temp:
#         temp.append(val)
#         res[key]=val
# print("The dictionary after removing the duplicates is:",res)



#6. Write a Python program to remove spaces from dictionary keys.
# student_list = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
# print("Original dictionary: ",student_list)
# student_dict = {x.translate({32: None}): y for x, y in student_list.items()}
# print("New dictionary: ",student_dict)
#

#7. Write a Python program to get the maximum and minimum value in a dictionary.

# marks = {"m1": 78, "m2": 89, "m3": 64, "m4": 35, "m5": 71, "m6": 135,"m7": 13}
#
# v = marks.values()
# maxi = max(v)
# mini = min(v)
#
# print("Maximum :", maxi)
# print("Minimum :", mini)


#8. Write a Python program to check a dictionary is empty or not.
# myDict = {}
# if not myDict:
#     print('The dictionary is empty.')
# else:
#     print('The dictionary is not empty.')

# второй вариант
# my_dict = {}
#
# if not bool(my_dict):
#     print("Dictionary is empty")

# третий вариант
# myDict = {12:25}
# if (len(myDict) == 0):
#     print('The dictionary is empty.')
# else:
#     print('The dictionary is not empty.')

# 9.Write a Python program to combine two dictionary adding values for common keys.
# dict1 = {'a': 100, 'b': 200, 'c':300}
# dict2 = {'a': 300, 'b': 200, 'd':400}
#
# c = {i: dict1.get(i, 0) + dict2.get(i, 0)
#      for i in set(dict1).union(dict2)}
# print(c)
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
#10. Write a Python program to print a dictionary line by line.
# student_score = {'Ritika': 5, 'Sam': 7, 'John': 10,'Aadi': 8}
# # Iterate over the key-value pairs of a dictionary
# # using list comprehension and print them
# [print(key,':',value) for key, value in student_score.items()]
# # or
# student_score = {'Ritika': 5, 'Sam': 7, 'John': 10,'Aadi': 8}
# # Iterate over key/value pairs in dict and print them
# for key, value in student_score.items():
#     print(key, ' : ', value)


# Rewrite all exercises using functions
