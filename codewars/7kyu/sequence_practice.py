def sum_of_n(n):
    res = []
    for i in range(n+1):
        res.append(i)
    sol = [0] * (n + 1)
    for i in range(len(res)):
        sol[i] = sum(res[:i+1])
    return sol


def range_(n):
    if n > 0:
        return range(n+1)
    else:
        return [-i for i in range(-n+1)]


def sum_of_n_2(n):
    return [sum(range_(i)) for i in range_(n)]


if __name__ == "__main__":
    print(sum_of_n_2(-3))
