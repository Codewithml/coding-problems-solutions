def reverse_letter(string):
    return "".join([i for i in reversed(string) if i.isalpha()])


if __name__ == "__main__":
    print(reverse_letter("krishan34"))
