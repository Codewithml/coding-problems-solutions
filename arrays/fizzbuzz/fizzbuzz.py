class FizzBuzz(object):
    def fizzbuzz(self, number):
        if number is None:
            raise TypeError
        if number < 1:
            raise ValueError
        res = []
        for i in range(1, number+1):
            if(i % 3 == 0 and i % 5 == 0):
                res.append("FizzBuzz")
            elif (i % 3 == 0):
                res.append("Fizz")
            elif (i % 5 == 0):
                res.append("Buzz")
            else:
                res.append(str(i))
        return res
