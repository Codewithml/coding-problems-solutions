def triangular(n):
    if n < 0:
        return 0
    return (n * (n + 1))//2


if __name__ == "__main__":
    print(triangular(-9))
