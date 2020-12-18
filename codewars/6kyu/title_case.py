def title_case(title, minor_words=''):
    if minor_words == '':
        return title.title()
    title = title.lower().split()
    words = minor_words.lower().split()
    title[0] = title[0].title()
    for i in range(1, len(title)):
        if title[i] in words:
            title[i] = title[i].lower()
        else:
            title[i] = title[i].title()
    return " ".join(title)


if __name__ == "__main__":
    print(title_case('a clash of KINGS', 'a an the of'))
