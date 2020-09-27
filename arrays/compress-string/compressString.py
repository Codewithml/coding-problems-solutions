class CompressString(object):
    def compress(self, input):
        if input is None or not input:
            return input
        result = ''
        count = 0
        prev_char = input[0]
        for char in input:
            if char == prev_char:
                count += 1
            else:
                result += prev_char + (str(count) if count > 1 else '')
                prev_char = char
                count = 1
        result += prev_char + (str(count) if count > 1 else '')
        return result if len(result) < len(input) else input
