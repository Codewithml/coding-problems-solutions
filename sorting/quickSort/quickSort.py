class QuickSort(object):

    def quickSort(self, data):
        if data is None:
            raise TypeError("can't be None")
        if len(data) < 2:
            return data
        equal = []
        left = []
        right = []
        pivot_ind = len(data) // 2
        pivot = data[pivot_ind]
        for i in data:
            if i == pivot:
                equal.append(i)
            elif i < pivot:
                left.append(i)
            else:
                right.append(i)
        left_ = self.quickSort(left)
        right_ = self.quickSort(right)

        return left_ + equal + right_
