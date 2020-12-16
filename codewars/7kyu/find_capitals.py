def find_capitals(word):
    res = []
    for i in range(len(word)):
        if word[i].isupper():
            res.append(i)
    return res


if __name__ == "__main__":
    print(find_capitals("CodEWars"))
