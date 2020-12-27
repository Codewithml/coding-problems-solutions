def sum_of_n(n):
    res = []
    for i in range(n+1):
        res.append(i)
    sol = [0] * (n + 1)
    for i in range(len(res)):
        sol[i] = sum(res[:i+1])
    return sol


if __name__ == "__main__":
    print(sum_of_n(3))
