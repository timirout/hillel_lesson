class frange:
    def __init__(self, left, right=None, step=None):
        self._left = left
        self._right = right if right else 0
        self._step = step

        if self._right == 0:
            self._left, self._right = self._right, self._left
        if not step:
            if self._left <= self._right:
                self._step = 1
            else:
                self._step = -1

    def __next__(self):
        if self._left > self._right:
            if self._left + self._step < self._right:
                raise StopIteration('stop')
        else:
            if self._left + self._step > self._right:
                raise StopIteration('stop')
        result = self._left
        self._left += self._step
        return result

    def __iter__(self):
        return self


# for i in frange(10):
#     print(i)


assert(list(frange(5)) == [0, 1, 2, 3, 4])
assert(list(frange(2, 5)) == [2, 3, 4])
assert(list(frange(2, 10, 2)) == [2, 4, 6, 8])
assert(list(frange(10, 2, -2)) == [10, 8, 6, 4])
assert(list(frange(2, 5.5, 1.5)) == [2, 3.5, 5])
assert(list(frange(1, 5)) == [1, 2, 3, 4])
assert(list(frange(0, 5)) == [0, 1, 2, 3, 4])
assert(list(frange(0, 0)) == [])
assert(list(frange(100, 0)) == [])

print('SUCCESS!')


# def generator_1(a, b):
#     while True:
#         yield a * b
#         a = a + 1


# gen = generator_1(2, 5)

# print(dir(gen))
