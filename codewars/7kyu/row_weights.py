def row_weights(array):
    odd = []
    even = []
    for i in range(len(array)):
        if i % 2 == 0:
            even.append(array[i])
        else:
            odd.append(array[i])
    return sum(even), sum(odd)


def row_weights_2(array):
    return sum(array[::2]), sum(array[1::2])


if __name__ == "__main__":
    print(row_weights_2([100, 50]))
