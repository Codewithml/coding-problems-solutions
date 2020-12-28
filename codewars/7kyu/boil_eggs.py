import math


def cooking_time(eggs):
    mins = 0
    while eggs > 0:
        eggs -= 8
        mins += 5
    return mins


def cooking_time_2(eggs):
    return 5 * math.ceil(eggs/8.0)


if __name__ == "__main__":
    print(cooking_time(0))
