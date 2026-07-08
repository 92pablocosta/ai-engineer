# main program
from functions import *

numbers = [4, 20, 5, 99, 1]

# while True:
#     try:
#         number = int(input('Type a number: '))
#     except:
#         print('This is not a valid number. Try again.')
#     else:
#         numbers.append(number)
#     finally:
#         option = input('Would you like to add another number? [y/n]: ').strip().lower()
#         if 'n' in option:
#             break

print(numbers)
print(f'The largest number is: {max(numbers)}')
print(f'The smallest number is: {min(numbers)}')
print(f'Sum of the numbers: {sum(numbers)}')
print(f'Average of the numbers: {calculateAverage(numbers)}')