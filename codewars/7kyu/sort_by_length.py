def sort_by_length(arr):
    return sorted(arr, key=len)


if __name__ == "__main__":
    print(sort_by_length(["Telescopes", "Glasses", "Eyes", "Monocles"]))
