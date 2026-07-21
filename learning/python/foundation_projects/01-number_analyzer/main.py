from functions import *

numbers = list()

while True:
    try:
        number = int(input('Type a number: '))
    except ValueError:
        print('This is not a valid number. Try again.')
    else:
        numbers.append(number)
    finally:
        while True:
            option = input('Would you like to add another number? [y/n]: ').strip().lower()
            if option in ['y', 'n']:
                break
            elif option != 'y':
                print('Invalid option. Please type y or n.')

print(numbers)
print(f'The largest number is: {max(numbers)}')
print(f'The smallest number is: {min(numbers)}')
print(f'Sum of the numbers: {sum(numbers)}')
print(f'Average of the numbers: {calculateAverage(numbers)}')
print(f'Even numbers: {evenNumbers(numbers)}')
print(f'Odd numbers: {oddNumbers(numbers)}')
print(f'Numbers in ascending order: {sorted(numbers)}')
