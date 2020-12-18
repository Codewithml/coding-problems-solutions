def two_sum(numbers, target):
    for i in range(len(numbers)):
        for j in range(1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return i, j


def two_sum_2(numbers, target):
    res = {}
    for i in range(len(numbers)):
        if target - numbers[i] in res:
            return [res[target - numbers[i]], i]
        else:
            res[numbers[i]] = i


if __name__ == "__main__":
    print(two_sum_2([1, 2, 3], 4))
