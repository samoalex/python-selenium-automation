# User inputs two numbers. One number is assigned to a variable, the other number is assigned to
# another variable. The task is to invert the variables, so that the first variable contains the second number,
# while the first number is in the second variable.

# a = int(input('Input value a: '))
# b = int(input('Input value b: '))
#
# print(f'a = {a}, b = {b}')

# c = b
# b = a
# a = c

# a = a + b
# b = a - b
# a = a - b

# a, b = b, a
# print(f'a = {a}, b = {b}')


#######Factorial#############################################################
# When User enters a number, its factorial is displayed.
import math

# n = int(input('Input a number: '))
# def factorial(number):
#     result = 1
#
#     if number < 0:
#         return f'Are you shure you\'d like to calculate gamma-functions?'
#     for item in range(1,number + 1):
#         print(item)
#         result *= item
#     return result
#
#
# print(factorial(n))


# 2 variant
# n = int(input('Input a number: '))
# def factorial(number):
#     return math.factorial(number)
# print(factorial(n))

##########Sum of three digit numbers################################
#Our code generates a random three-digit number and has to sum up all its digits.
# For example, if a number is 349, the code has to print the number 16, because 3 + 4 + 9 = 16.
#Сложение чисел одного числа
# from random import randint
#
# n = randint(100, 999)
# print(n)#634
#
# ones = n % 10 #4
# tens = (n //10) % 10 #3
# hundrets = n // 100 #6
# print(ones + tens + hundrets) #Sum 13

####################Home Work#################################
#Rewrite a program with any number of digits.
#Instead of 3 digits, you should sum digits up from n digits number,
#Where User enter n manually. n > 0 (n = 6 количество знаков в заданном числе)

#######################Leap Year########################################
#When a user enters a year, the code detects if it is a leap year or not.

# Leap years have the following characteristics:
# Their number is multiple by 400 or their number is multiple by 4.
# If the year number id multiple by 100, it is not a leap year.
#
# We should IF-statements to detect if it is a leap year or not.

# year = int(input('Enter a year: '))
#
# if year % 4 != 0:
#     print('Not leap year')
# else:
#     if year % 100 != 0:
#         print('Leap year')
#     else:
#         if year % 400 == 0:
#              print('Leap year')
#         else:
#             print('Leap year')

###########Binary ################################################

# Find the maximal sequence of consecutive zeros that surrounded by ones at both ends in the binary representation of a number entered by User.
#
# Binary gap is the maximal sequence of consecutive zeros that surrounded by ones at both ends in a binary number.
#
# Examples:
# 9 as a binary number is 1001. The Binary gap is equal to 2 (there are two consecutive zeros in this number).
# 529 as a binary number is 1000010001. The Binary gap is equal to 4.
#
#n = int(input('Input a number: '))

# def to_bin(number):
#     bin_string = ''
#     while number > 0:
#         bin_string += str(number % 2)
#         number = number // 2
#     return bin_string[::-1]
# print(to_bin(n))
#####or######

# n = int(input('Input a number: '))
# print(bin(n))

####################binary gap#####################

# n = int(input('Input a number: '))
#
# def to_bin(number):
#     bin_string = ''
#     while number > 0:
#         bin_string += str(number % 2)
#         number = number // 2
#     return bin_string[::-1]
#
# #10001
# print(f'binary number{to_bin(n)}')
# print(f'binary number from bin function {bin(n)}')
# def binary_gap(bin_number):
#     max_gap = 0
#     counter = 0
#
#     for digit in bin_number:
#         if digit == '1':
#             if max_gap < counter:
#                 max_gap = counter
#             counter = 0
#         else:
#             counter += 1
#     print(max_gap)
#
# binary_gap(to_bin(n))
# print(bin(13))
# print(bin(13)[2:])
#####################Home Work#######################################################
# Sum of 3 modified
# # TODO: Homework: Rewrite a program with any number of digits.
# #  Instead of  3 digits, you should sum digits up from n digits number,
# #  Where User enter n manually. n > 0
#
# Find max number from 3 values, entered manually from a keyboard
#
# Count odd and even numbers.  Count odd and even digits of the whole number. E.g, if entered number 34560, then 3 digits will be even (4, 6, and 0)  and  2 odd digits (3 and 5).
#
# Codewars.com (3-4 problems)

#1.Find max number from 3 values, entered manually from a keyboard
# num1 = int(input(f"First number "))
# num2 = int(input(f"Second number "))
# num3 = int(input(f"Third number "))
#
# def max_of_three(number_1, number_2, number_3):
#     if number_1 > number_2:
#          if number_1 > number_3:
#              print(f'The greatest number in range is {number_1}')
#          else:
#              print(f'The greatest number in range is {number_3}')
#     else:
#         if number_2 > number_3:
#              print(f'The greatest number in range is {number_2}')
#         else:
#              print(f'The greatest number in range is {number_3}')
#
#
#
#
# max_of_three(num1, num2, num3)


#2.Count odd and even numbers.  Count odd and even digits of the whole number.
# E.g, if entered number 34560, then 3
# digits will be even (4, 6, and 0)  and  2 odd digits (3 and 5).

# number = int(input(f'Enter a number: '))
#
#
# def count_odd_even(n):
#     odd_counter = 0
#     even_counter = 0
#     while n > 0:
#         digit = n % 10
#         if digit % 2 == 0:
#             even_counter += 1
#         else:
#              odd_counter += 1
#         n = n // 10
#     print(odd_counter)
#     print(even_counter)
#
# count_odd_even(number)

#3.Rewrite a program with any number of digits.
# Instead of  3 digits, you should sum digits up from n digits number,
#  Where User enter n manually. n > 0
from random import randint

n = int(input(f'Enter a number of digits: '))



def sum_of_digits(digits):
    if digits < 1:
        print('Wrong value. Number should contain at last 1 digit')
        quit()
    down = 10 ** (digits - 1)
    up = 10 ** digits - 1
    n = randint(down,up)
    print(f'We got the number {n}')

    result = 0
    i = 0
    while i < digits:
        result += n % 10
        n = n // 10
        i += 1
    print(f'The result is {result}')

sum_of_digits(n)