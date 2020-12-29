def nb_dig(n, d):
    squ = [(i*i) for i in range(n+1)]
    count = 0
    for i in squ:
        if str(i).count(str(d)):
            count += str(i).count(str(d))
    return count


def nb_dig_2(n, d):
    return sum(str(i*i).count(str(d)) for i in range(n+1))


if __name__ == "__main__":
    print(nb_dig_2(5750, 0))
