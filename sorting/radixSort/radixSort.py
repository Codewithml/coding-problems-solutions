class RadixSort(object):

    def radixSort(self, data, base=10):
        if data is None:
            raise TypeError("can't be None")
        if len(data) < 2:
            return data
        max_element = max(data)
        max_digit = len(str(abs(max_element)))
        curr_data = data
        for digit in range(max_digit):
            buckets = [[] for _ in range(base)]
            for item in curr_data:
                buckets[(item // (base**digit)) % base].append(item)
            curr_data = []
            for bucket in buckets:
                curr_data.extend(bucket)
        return curr_data
