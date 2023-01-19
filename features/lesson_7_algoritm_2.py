# #1.Circle : input radius, get area
# def circle_area(radius):
#     return radius ** 2 * math.pi
#
# print(circle_area(3))
#
# #2. Rectangle: input height and width, get area
# def rectangle_area(height, width):
#     return (height * width)
#
# print(rectangle_area(3 , 9))
#
# #3. Square: input width, get area
# def square_area(width):
#     return width ** 2
#
# print(square_area(10))

# 4. You have a dictionary of cities. Create dictionary of distances
# Distance in 2D space =  ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

# from pprint import pprint
# cities = {
# 	'Los Angeles': (550, 370),
# 	'Chicago': (510, 510),
# 	'Dallas': (480, 480),
# }
#
# distances = {}
#
# los_angeles = cities['Los Angeles']
# chicago = cities['Chicago']
# dallas = cities['Dallas']
#
# los_angeles_chicago = ((chicago[0] - los_angeles[0]) ** 2 + (chicago[1] - los_angeles[1]) ** 2) ** 0.5
# chicago_dallas = ((chicago[0] - dallas[0]) ** 2 + (chicago[1] - dallas[1]) ** 2) ** 0.5
# los_angeles_dallas = ((los_angeles[0] - dallas[0]) ** 2 + (los_angeles[1] - dallas[1]) ** 2 ) ** 0.5
#
#
# distances['Los Angeles'] = {}
# distances['Los Angeles'] ['Dallas'] = los_angeles_dallas
# distances['Los Angeles'] ['Chicago'] = los_angeles_chicago
#
#
# distances['Chicago'] = {}
# distances['Chicago'] ['Dallas'] = chicago_dallas
# distances['Chicago'] ['Los Angeles'] = los_angeles_chicago
#
#
# distances['Dallas'] = {}
# distances['Dallas'] ['Los Angeles'] = los_angeles_dallas
# distances['Dallas'] ['Chicago'] = chicago_dallas
#
# pprint(distances)

# 5. Multiplication - Write function which use two digits and count multiplication.
# You must not use * operation
# Multiplication is repetition a sum of number a b times.
# 7 * 3 = 7 + 7 + 7 = 3 + 3 + 3 + 3 + 3 + 3 + 3


# def multiplication(number_1, number_2):
# 	iterator = 0
# 	result = 0
# 	while iterator < number_1:
# 		result += number_2
# 		iterator += 1
# 	return result
#
# print(multiplication(359,359))
# print(359 * 359)

# 6.Seconds to h:m:s - Write function, which will convert seconds to format h:m:s
# n one minute we have 60 seconds
# In one hour we have 60 minutes = 60 * 60 = 3600 seconds

# def sec_to_hms(seconds):
# 	hours = seconds // 3600
# 	seconds = seconds - hours * 3600
# 	minutes = seconds // 60
# 	seconds = seconds - minutes * 60
# 	return (f'{hours}:{minutes}:{seconds}')
#
#
#
# print(sec_to_hms(10000))
#
# 7.Fibonacci sequence
# The equation for the Fibonacci sequence:
# φ0 = 0,  φ1 = 1,  φn = φn−1 + φn−2.
# The task is to display all the numbers from start to n of the Fibonacci sequence φn
# 1, 1, 2, 3, 5, 8 …
# F3 = F2 + F1 = 1 + 1 = 2
# F4 = F3 + F2 = 2 + 1 = 3
# F5 = F4 + F3 = 3 + 2 = 5
# F6 = F5 + F4 = 5 + 3 = 8

# Equation:
# F0 = 0
# F1 = 1
# F2 = 1
# Fn = Fn-1 + Fn-2


def fibanachi(n):
    fibanachi_1 = 1
    fibanachi_2 = 1

    if n == 0:
        print(0)
    if n > 0:
        print(fibanachi_1)
    if n > 1:
        print(fibanachi_2)
        index = 0
        while index < n - 2:
            fibanachi_1, fibanachi_2 = fibanachi_2, fibanachi_1 + fibanachi_2
            index += 1
            print(fibanachi_2)

fibanachi(10)
