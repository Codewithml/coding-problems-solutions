def iq_test(numbers):
    res = [int(i) % 2 for i in numbers.split()]
    if res.count(0) > 1:
        return res.index(1) + 1
    else:
        return res.index(0) + 1


if __name__ == "__main__":
    print(iq_test("1 2 2"))
