def evaporator(content, evap_per_day, threshold):
    count = 0
    start = 100
    while start > threshold:
        start -= start * (evap_per_day/100)
        count += 1
    return count


if __name__ == "__main__":
    print(evaporator(10, 10, 10))
