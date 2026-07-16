def calculateAverage(numbers=[]) -> str:
    average = sum(numbers) / len(numbers)
    return f'{average:.1f}'


def evenNumbers(numbers=[]) -> list:
    even_numbers = list()
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers


def oddNumbers(numbers=[]) -> list:
    odd_numbers = list()
    for number in numbers:
        if number % 2 != 0:
            odd_numbers.append(number)
    return odd_numbers
