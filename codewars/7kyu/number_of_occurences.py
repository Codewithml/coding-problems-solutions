from collections import defaultdict


def number_of_occurrences(element, sample):
    res = defaultdict(int)
    for i in sample:
        if i in res:
            res[i] += 1
        else:
            res[i] = 1
    return res[element]


if __name__ == "__main__":
    sample = [0, 1, 2, 2, 3]
    print(number_of_occurrences(4, sample))
