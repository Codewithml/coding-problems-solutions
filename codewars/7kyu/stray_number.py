def stray_number(arr):
    for i in arr:
        if arr.count(i) == 1:
            return i


if __name__ == "__main__":
    print(stray_number([17, 17, 3, 17, 17]))
