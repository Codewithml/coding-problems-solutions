def mexican_wave(word):
    res = []
    split_s = list(word)
    for i in range(len(word)):
        if split_s[i].isspace():
            continue
        elif split_s[i].isalpha():
            split_s[i] = word[i].upper()
            res.append("".join(split_s))
            split_s[i] = word[i].lower()
    return res


if __name__ == "__main__":
    print(mexican_wave("  hello  "))
