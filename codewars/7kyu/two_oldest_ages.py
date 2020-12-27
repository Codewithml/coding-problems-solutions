def two_oldest_ages(ages):
    ages = sorted(ages)
    return ages[-2:]


if __name__ == "__main__":
    print(two_oldest_ages([1, 5, 87, 45, 8, 8]))
