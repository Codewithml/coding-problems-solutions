class BubbleSort(object):

    def bubbleSort(self, data):
        if data is None:
            raise TypeError("can't be none")
        if len(data) < 2:
            return data
        for i in range(len(data)):
            swapped = False
            for j in range(len(data) - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
                    swapped = True
            if swapped is False:
                break
        return data
