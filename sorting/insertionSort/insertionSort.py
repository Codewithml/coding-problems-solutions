class InsertionSort(object):

    def insertionSort(self, data):
        if data is None:
            raise TypeError("can't be None")
        if len(data) < 2:
            return data
        for i in range(1, len(data)):
            for j in range(i):
                if data[i] < data[j]:
                    temp = data[i]
                    data[j+1:i+1] = data[j:i]
                    data[j] = temp
        return data
