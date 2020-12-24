class MergeSort(object):

    def mergeSort(self, data):
        if data is None:
            raise TypeError("can't be None")
        if len(data) < 2:
            return data
        mid = len(data) // 2
        left = data[:mid]
        right = data[mid:]
        left = self.mergeSort(left)
        right = self.mergeSort(right)
        l = 0
        r = 0
        k = 0
        while l < len(left) and r < len(left):
            if left[l] < right[r]:
                data[k] = (left[l])
                l += 1
            else:
                data[k] = (right[r])
                r += 1
            k += 1
        while l < len(left):
            data[k] = (left[l])
            l += 1
            k += 1
        while r < len(right):
            data[k] = (right[r])
            r += 1
            k += 1
        return data
