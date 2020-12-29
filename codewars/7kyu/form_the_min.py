def min_value(digits):
    res = []
    digits = set(digits)
    for i in range(len(digits)):
        res.append(min(digits))
        digits.remove(min(digits))
    return int("".join(str(i) for i in res))


def min_value_2(digits):
    return int("".join(map(str, sorted(set(digits)))))


if __name__ == "__main__":
    print(min_value_2([1, 3, 1]))
