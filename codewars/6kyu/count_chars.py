def count_chars(string):
    if string is None:
        return {}
    res = {}
    for i in string:
        res[i] = string.count(i)
    return res


if __name__ == "__main__":
    print(count_chars("aba"))
