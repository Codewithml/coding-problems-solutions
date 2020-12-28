def get_even_numbers(arr):
    return [i for i in arr if i % 2 == 0]


if __name__ == "__main__":
    print(get_even_numbers([2, 4, 5, 6]))
