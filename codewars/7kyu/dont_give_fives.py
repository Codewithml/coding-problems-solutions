def dont_give_me_five(start,end):
    counter = 0
    for i in range(start, end + 1):
        if '5' in str(i):
            continue
        else:
            counter += 1
    return counter


if __name__ == "__main__":
    print(dont_give_me_five(1, 9))
