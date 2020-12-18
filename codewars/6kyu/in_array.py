def in_array(array1, array2):
    res = []
    for i in array1:
        for j in array2:
            if i in j:
                res.append(i)
    return sorted(list(set(res)))


if __name__ == "__main__":
    a1 = ["live", "arp", "strong"]
    a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
    print(in_array(a1, a2))
