import math


def divisors(n):
    res = 0
    for i in range(1, int(math.sqrt(n) + 1)):
        if (n % i == 0):
            if (n / i == i):
                res += 1
            else:
                res += 2
    return res


def divisors_2(n):
    return sum([n % x == 0 for x in range(1, n+1)])


if __name__ == "__main__":
    print(divisors_2(12))
