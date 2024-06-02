from statistics import mean


def improve_average(numbers):
    minimal, average = min(numbers), mean(numbers)
    while minimal < average:
        print(f'The mean of {numbers} is {average:.2f}')
        print(f'Remove {minimal}')
        numbers.remove(minimal)
        minimal, average = min(numbers), mean(numbers)


improve_average([6, 9, 5, 2, 4, 3])