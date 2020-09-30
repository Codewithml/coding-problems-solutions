class ValidElements(object):
    def validElements(self, arr):
        if not arr:
            return 0
        return len(set(arr))

    def validElements2(self, arr):
        if not arr:
            return 0
        seen = {}
        for entry in arr:
            if entry not in seen:
                seen[entry] = 1
        return len(seen)

    def validElements3(self, arr):
        if not arr:
            return 0
        index = 1
        for i in range(1, len(arr)):
            if arr[index - 1] != arr[i]:
                arr[index] = arr[i]
                index += 1
        return index
