import array
from datetime import date as day

name = "Mike"
tuple = ('a', 2, 'hello', 3.5)
list = ['a', 2, 'hello', 3.5]
new_array = array.array('i', [1, 2, 3])
car = {
    'make': 'ford',
    'model': 'focus',
    'year': 2017
}

car['year'] = 2018
# print(car)

number = -5

# if number < 0:
#     print('number is negative')
#     number = number * -1
# elif number > 0:
#     print('number is positive')
# else:
#     print('number is 0')

# print(number)


numbers = [1, 2, 3, 4, 5]
# sum = 0
# i = 0
# while i < len(numbers):
#     sum += numbers[i]
#     i += 1
# print(f'The sum of the numbers array is {sum}')

# print(sum(numbers))

# sum=0
# for number in numbers:
# 	sum+=number

# for i in range(5):
#     if i == 2:
#         continue
#     print(i)

# print(f'The sum of the numbers array is {sum}')


def fibonacci(n:int)->list:
    '''Gets the first few numbers of the fibonacci sequence'''
    a = 0
    b = 1
    sequence = [0]
    while b <= n:
        sequence.append(b)
        c = a+b
        a = b
        b = c
    return sequence


# print(fibonacci(100))

print(day.today())