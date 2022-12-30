# string_1 = 'I like Python'
# result = string_1[7:13]
# print(len(string_1))
# print(string_1[-2])
# print(string_1[len(string_1)-2])
# print(result)
# result = string_1.index('P')
# # result = string_1.index('P', 2, 13)
# print(result)

#Range
# range_1 = range(10)# 0,1,2,3,4,5,6,7,8,9
# range_2 = range(5,15)
# range_3 = range(2,20,4) #2,6,10,14,18

# While loop
# index = 0
# while index < 10:
#     print(index)
#     index += 1

# For loop
# for char in string_1:
#     if char == 'P':
#         print('We have a "P" in a string')
#         break
#     print(char)

# list_1 = []
# list_2 =[1,2,3,4,5]
# list_3 = list(string_1)
#
# # print(list_2 + list_3)
# # print(list_3.count('e'))
# list_3.reverse()
# print(list_3)
#########################################################
######## HOME WORK 2 ####################################
# 1.Ask the user to enter their name and then display their name three times.
# name = input('Please enter your name: ')
# repeate = 0
# while repeate < 3:
#     print(name)
#     repeate += 1

# 2. Alter program 1 so that it will ask the user to enter their name and a number and
# then display their name that number of times.
# name = input('Please enter your name: ')
# number = int(input('Please enter any namber : '))
# repeate = 0
# while repeate < number:
#     print(name)
#     repeate += 1

# 3.Ask the user to enter their name and display each letter in their name on a separate line.
# name = input('Please enter your name: ')
# index = 0
# while index < len(name):
#     print(name[index])
#     index += 1

# 4.Change program 3 to also ask for a number. Display their name (one letter at a time on each line)
# and repeat this for the number of times they entered.

# name = input('Please enter your name: ')
# number = int(input('Please enter any namber: '))
# repeat = 0
#
# while repeat < number:
#      index = 0
#      while index < len(name):
#          print(name[index])
#          index += 1
#      repeat += 1

# 5.Ask the user to enter their name and a number. If the number is less than 10,
# then display their name that number of times; otherwise display the message “Too high” three times.






# 6.Set a variable called total to 0. Ask the user to enter five numbers and after each input ask them if they want that number included. If they do, then add the number to the total. If they do not want it included, don’t add it to the total. After they have entered all five numbers, display the total.
# 7.Ask which direction the user wants to count (up or down). If they select up, then ask them for the top number and then count from 1 to that number. If they select down, ask them to enter a number below 20 and then count down from 20 to that number. If they entered something other than up or down, display the message “I don’t understand”.
# 8.Ask how many people the user wants to invite to a party. If they enter a number below 10, ask for the names and after each name display “[name] has been invited”. If they enter a number which is 10 or higher, display the message “Too many people”.
# 9.Set the total to 0 to start with. While the total is 50 or less, ask the user to input a number. Add that number to the total and print the message “The total is… [total]”. Stop the loop when the total is over 50.
# 10.Ask the user to enter a number. Keep asking until they enter a value over 5 and then display the message “The last number you entered was a [number]” and stop the program.
# 11.Ask the user to enter a number and then enter another number. Add these two numbers together and then ask if they want to add another number. If they enter “y", ask them to enter another number and keep adding numbers until they do not answer “y”. Once the loop has stopped, display the total.
# 12.Ask for the name of somebody the user wants to invite to a party. After this, display the message “[name] has now been invited” and add 1 to the count. Then ask if they want to invite somebody else. Keep repeating this until they no longer want to invite anyone else to the party and then display how many people they have coming to the party.
# 13.Ask the user to enter a number between 10 and 20. If they enter a value under 10, display the message “Too low” and ask them to try again. If they enter a value above 20, display the message “Too high” and ask them to try again. Keep repeating this until they enter a value that is between 10 and 20 and then display the message “Thank you”.
# 14.Write a Python program to sum all the items in a list.
# list_1 = list(range(10))
# print(list_1)
# sum_value = 0
# for item in list_1:
#     sum_value += item
# print(sum_value)

# 15.Write a Python program to multiplies all the items in a list.
# list_1 = [10,2,3,4]
# print(list_1)
# sum_value = 1
# for item in list_1:
#     sum_value *= item
# print(sum_value)

# 16.Write a Python program to get the largest number from a list.
list_1 = [1, 2, 5, 99, -7, 6, 38, 7, 36]
max_value = list_1[0]
for number in list_1:
    if max_value < number:
        max_value = number

print(max_value)

# 17.Write a Python program to get the smallest number from a list
# 18.Write a Python program to remove duplicates from a list.
# 19.Write a Python program to check a list is empty or not.
# 20.Write a Python function that takes two lists and returns True if they have at least one common member.
# 21.Write a Python program to get unique values from a list.
# 22.Write a Python program to select the odd items of a list.
# 23.Write a Python program to concatenate elements of a list
