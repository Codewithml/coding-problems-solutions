def sum_triangular_numbers(n):
    if n < 0:
        return 0
    return sum([((i * (i + 1))//2) for i in range(n + 1)])


if __name__ == "__main__":
    print(sum_triangular_numbers(4))
