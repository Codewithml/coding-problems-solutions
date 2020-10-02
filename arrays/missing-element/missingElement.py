class MissingElement(object):
    def missingElement(self, arr1, arr2):
        count = {}
        for element in arr1:
            if element in count:
                count[element] += 1
            else:
                count[element] = 1
        for element in arr2:
            if element in count:
                count[element] -= 1
            else:
                count[element] = 1
        for k in count:
            if count[k] != 0:
                return k

    def missingElement2(self, arr1, arr2):
        result = 0
        for element in arr1 + arr2:
            result ^= element
        return result

    def missingElement3(self, arr1, arr2):
        arr1.sort()
        arr2.sort()
        for ele1, ele2 in zip(arr1, arr2):
            if ele1 != ele2:
                return ele1
        return arr1[-1]

    def missingElement4(self, arr1, arr2):
        return abs(sum(arr1) - sum(arr2))
