def sequence_sum(begin_number, end_number, step):
    # res = [i for i in range(begin_number, end_number + 1)]
    # return sum(res[::step])
    return sum(range(begin_number, end_number + 1, step))


if __name__ == "__main__":
    print(sequence_sum(2, 2, 2))
