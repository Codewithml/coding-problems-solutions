def pattern(n):
    if n < 1:
        return ""
    res = []
    for i in range(1, n+1):
        res.append(f"{i}" * i)
    return "\n".join(res)


if __name__ == "__main__":
    print(pattern(3))
