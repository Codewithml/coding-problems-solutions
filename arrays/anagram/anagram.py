class Anagram(object):

    def anagram(self, string1, string2):
        if string1 is None or string2 is None:
            return None
        string1 = string1.replace(" ", "").lower()
        string2 = string2.replace(" ", "").lower()
        count = {}
        for let in string1:
            if let in count:
                count[let] += 1
            else:
                count[let] = 1
        for let in string2:
            if let in count:
                count[let] -= 1
            else:
                count[let] = 1
        for k in count:
            if count[k] != 0:
                return False
        return True

    def anagram2(self, string1, string2):
        if string1 is None or string2 is None:
            return None
        string1 = string1.replace(" ", "").lower()
        string2 = string2.replace(" ", "").lower()
        return sorted(string1) == sorted(string2)
