def number(lines):
    return [f"{i+1}: {lines[i]}" for i in range(len(lines))]


if __name__ == "__main__":
    print(number(["a", "b", "c"]))
