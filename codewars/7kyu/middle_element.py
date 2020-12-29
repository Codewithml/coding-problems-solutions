def gimme(input_array):
    temp = sorted(input_array)
    return input_array.index(temp[1])


if __name__ == "__main__":
    print(gimme([2, 3, 1]))
