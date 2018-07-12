#Square Numbers Series

class snseries:
    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.limit:
            result = self.n ** 2
            self.n += 1
            return result
        else:
            raise StopIteration


for element in snseries(10):
    print(element)

'''
Output:

0
1
4
9
16
25
36
49
64
81
100
'''