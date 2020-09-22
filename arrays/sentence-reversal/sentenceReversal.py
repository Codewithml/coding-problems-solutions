class SentenceReversal(object):
    def sentenceReversal(self, string):
        if string is None:
            return None
        words = string.split()
        size = len(words)
        for word in range(size//2):
            words[word], words[size - 1 - word] = \
                words[size - 1 - word], words[word]
        return " ".join(words)

    def sentenceReversal2(self, string):
        if string is None:
            return None
        words = []
        size = len(string)
        spaces = [' ']
        i = 0

        while i < size:
            if string[i] not in spaces:
                word_start = i
                while i < size and string[i] not in spaces:
                    i += 1
                words.append(string[word_start:i])
            i += 1
        return " ".join(words[::-1])

    def sentenceReversal3(self, string):
        if string is None:
            return None
        return " ".join(string.split()[::-1])
