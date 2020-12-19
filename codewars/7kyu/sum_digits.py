def sum_digits(number):
    number = number if number > 0 else -number
    if number == 0:
        return number
    sum = 0
    while(number > 0):
        sum += number % 10
        number //= 10
    return sum


if __name__ == "__main__":
    print(sum_digits(-678))
