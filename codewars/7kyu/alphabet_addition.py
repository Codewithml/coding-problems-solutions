def add_letters(*letters):
    if not letters:
        return 'z'
    sum = 0
    for i in letters:
        sum += ord(i) - 96
        if sum > 26:
            sum -= 26
    return chr(sum + 96)


if __name__ == "__main__":
    print(add_letters('y', 'c', 'b'))
