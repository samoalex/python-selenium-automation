import math
import time
# from Tools.demo.beer import n

#1. Write a Python program to calculate the area of a rectangle.

# a = 2
# b = 5
#
# area = a * b
# print(area)

#2. Write a Python program to calculate the area of a circle

# r = 10
# pi = math.pi
#
# area_circle = pi * r ** 2
# print(round(area_circle, 2))

# 3.Ask for the user’s first name and display the output message Hello [First Name].

# first_name = input("Please Insert Your Name : ")
# print('Hello '+ first_name + "!")

# 4.Ask the user to enter two numbers. Add them together and display the answer as The total is [answer].

# number_1 = input('Enter first number:')
# number_2 = input('Enter second number:')
# result = int(number_1) + int(number_2)
# print(type(result))
# print(result)
# print('The total is = ' + str(result))

# 5.Ask the user to enter three numbers. Add together the first two numbers and then multiply this total by the third. Display the answer as The answer is [answer].

# number_1 = int(input('Enter first number:'))
# number_2 = int(input('Enter second number:'))
# number_3 = int(input('Enter third number:'))
#
# result = (number_1 + number_2) * number_3
#
# print('The answer is: ' + str(result))

# 6.Ask the user for their name and their age. Add 1 to their age and display the output [Name]
# next birthday you will be [new age].

# name = input("Please Enter Your Name : ")
# age = int(input('Enter your age: '))
# age = age + 1
# print(name + ' next birthday you will be ' + str(age) + ' years old' )

# 7.Ask an integer number, check is it odd or even and return answer

# number_1 = int(input('Enter number:'))
#
# if (number_1 % 2 == 0):
#     print( str(number_1) + ' this even number')
# else:
#     print( str(number_1) + ' this odd number')

# 8.Ask the user to type in any word and display it in upper case. (See string methods)
# word = input('Enter eny word: ')
# print(word.upper())

# 9.Ask for the user’s first name and then ask for their surname and display the output message Hello
# [First Name] [Surname]

# first_name = input('What is your first name: ')
# last_name = input('What is your last name: ')
# print('Hello ' + first_name.upper() + ' ' + last_name.upper() + ' !')

#10. Write code that will display the joke “What do you call a bear with no teeth?” and on
# the next line display the answer “A gummy bear!”  Try to create it using only one line of code.
# print('What do you call a bear with no teeth?\n A gummy bear!')

# 11.Ask how many slices of pizza the user started with and ask how many slices they have eaten.
# Work out how many slices they have left and display the answer in a user-friendly format

# start_slices = int(input('How many slices of pizza were there? '))
# eaten_slices = int(input('How many slices did you eaten? '))
# result = start_slices - eaten_slices
# print('You have '+ str(result))

# 12.Ask for the total price of the bill, then ask how many diners there are.
# Divide the total bill by the number of diners and show how much each person must pay.

# total_bill = float(input('What the total price of the bill? '))
# total_diners = int(input('How many diners there are? '))
# result = round(total_bill/total_diners,2)
# total_result = result * 1.15
# total_result = round(total_result,2)
# print('Every person must pay: '+ str(result) + ' Plus 15% service fee. The total amount is: ' + str(total_result))

#13. Write a program that will ask for a number of days and then will show how many hours,
# minutes and seconds are in that number of days.

# day = int(input('Enter quantity of day: '))
# hours = day * 24
# sec = hours * 60
# print('In this number of days ' + str(hours) + ' hours or ' + str(sec) + ' seconds')

# 14.Task the user to enter a number over 100 and then enter a number under 10 and tell them how many
# times the smaller number goes into the larger number in a user-friendly format.
# number = int(input('Please enter a number over 100: '))
# number_1 = int(input('Please enter a number under 10: '))
# result = number // number_1
# print(print('Number ' + str(number) + ' contains ' + str(result) + ' numbers ' + str(number_1)))

# 15.Ask the integer number and return the second power of this number.
# number = int(input('Please enter a number : '))
# second_power = number ** 2
# therd_power = number ** 3
# forth_power = number ** 4
# print('Second power of ' + str(number) + ' = ' + str(second_power))
# print('Therd power of ' + str(number) + ' = ' + str(therd_power))
# print('Forth power of ' + str(number) + ' = ' + str(forth_power))
# #
# 16.Ask the integer number and power what you would like to get. Return result

# number_1 = int(input('Please enter a number : '))
# number_2 = int(input('Please enter a power: '))
# power = number_1 ** number_2
#
# print('Power of ' + str(number_1) + ' = ' + str(power))

# 17.Ask the user to enter their first name and then display the length of their name.
# first_name = input("Please Insert Your Name : ")
# print (len(first_name))

# 18.Ask the user to enter their first name and then ask them to enter their surname.
# Join them together with a space between and display the name and the length of the whole name.
# first_name = input("Please Insert Your First Name : ")
# last_name = input('Please Insert Your Laast Name : ')
# print(first_name + " " + last_name)
# print (len(first_name + " " + last_name))


# 19.Ask the user to enter their first name and surname in lower case.
# Change the case to title case and join them together. Display the finished result.

# first_name = input("Please Insert Your First Name : ")
# last_name = input('Please Insert Your Laast Name : ')
# age = input('Please Insert Your age : ')
# result = f'{first_name.capitalize()} {last_name.capitalize()} is {age} years '
# result1 = (first_name.upper() + " " + last_name.upper()) + ' is ' + str(age) + ' years'
# print(result)
# print(result1)


#20. Enter a random string, which includes only digits. Write a function
# sum_digits which will find a sum of digits in this string

# number = input('Enter number:')
# def sum_digits(digit):
#     return sum(int(x) for x in digit if x.isdigit())
# print(sum_digits(number))


# 21.Ask the user to enter their favorite color. If they enter “red”,
# “RED” or “Red” display the message “I like red too”, otherwise display the message
# “I don’t like [color], I prefer red”.
color = input('Enter your favorite color: ')
# if color == 'RED' or color == 'Red':
if color.lower() == 'red':
    print('I like red too')
else:
    print('I don’t like ' + color + ', I prefer Red. ')


# 22.Ask the user’s age. If they are 18 or over, display the message
# “You can vote”, if they are aged 17, display the message “You can learn to drive”, if they are 16, display the message “You can buy a lottery ticket”, if they are under 16, display the message “You can go Trickor-Treating”.





#23. Ask the user to enter a number. If it is under 10,
# display the message “Too low”, if their number is between 10 and 20,
# display “Correct”, otherwise display “Too high”.



#24. Ask the user to enter 1, 2, or 3. If they enter a 1, display the message “Thank you”,
# if they enter a 2, display “Well done”, if they enter a 3, display “Correct”.
# If they enter anything else, display “Error message”.

