def partlist(arr):
    return [(" ".join(arr[:i+1]), " ".join(arr[i+1:])) for i in range(len(arr)-1)]


if __name__ == "__main__":
    print(partlist(["I", "wish", "I", "hadn't", "come"]))
