def partlist(arr):
    return [(" ".join(arr[:i]), " ".join(arr[i:])) for i in range(1, len(arr))]


if __name__ == "__main__":
    print(partlist(["I", "wish", "I", "hadn't", "come"]))
