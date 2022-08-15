def add(*numbers):
    print(numbers[0])
    sum = 0
    for number in numbers:
        sum += int(number)
    return sum

if __name__ == "__main__":
    print(add(5, 2, 3))