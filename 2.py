import os

def get_data():
    cwd = os.getcwd()

    # Initialize lists to hold the data
    data = []

    # Open the file and read its contents
    with open(cwd + '/inputs/2.txt', 'r') as file:
        for line in file:
            # Split the line into numbers and convert them to integers
            numbers = list(map(int, line.split()))
            # Append the list of numbers to the data list
            data.append(numbers)

    return data


def check_conditions(lst):

    # define conditions
    increasing = all(lst[i] < lst[i + 1] for i in range(len(lst) - 1))
    decreasing = all(lst[i] > lst[i + 1] for i in range(len(lst) - 1))
    difference = all(abs(lst[i] - lst[i + 1]) <= 3 for i in range(len(lst) - 1))

    if difference and (increasing or decreasing):
        return 1
    else:
        return 0 

def part1():
    data = get_data()

    a = 0
    for lst in data:
        a += check_conditions(lst)

    return a

def check_conditions_part2(lst):

    # define conditions
    increasing = all(lst[i] < lst[i + 1] for i in range(len(lst) - 1))
    decreasing = all(lst[i] > lst[i + 1] for i in range(len(lst) - 1))
    difference = all(abs(lst[i] - lst[i + 1]) <= 3 for i in range(len(lst) - 1))

    if difference and (increasing or decreasing):
        return 1
    else:
        violation_a = all(abs(lst[i] - lst[i + 2]) <= 3 and abs(lst[i] - lst[i + 2]) >=1 for i in range(len(lst) - 2))

        if violation_a:
            return 1

        else:
            return 0


def part2():
    data = get_data()

    a = 0
    for lst in data:
        a += check_conditions_part2(lst)

    return a

print("Answer to part 1:", part1())
print("Answer to part 2:", part2())
