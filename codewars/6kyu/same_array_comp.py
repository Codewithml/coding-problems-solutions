def comp(array1, array2):
    array1.sort()
    array2.sort()
    if array1 is None and array2 is None:
        return False
    elif len(array1) == 0 or len(array2) == 0:
        return True
    elif len(array1) != len(array2):
        return False
    res = []
    for i in range(len(array1)):
        if array1[i] ** 2 == array2[i]:
            res.append(True)
        else:
            False
    if res.count(False) > 0:
        return False
    return True


if __name__ == "__main__":
    a1 = [121, 144, 19, 161, 19, 144, 19, 11]
    a2 = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
    print(comp(a1, a2))
