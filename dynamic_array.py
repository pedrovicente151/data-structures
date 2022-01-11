import ctypes


class DynamicArray:
    """ Simplified Python List."""

    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def __len__(self):
        return self._n

    def __getitem__(self, item):
        if not 0 <= item < self._n:
            raise IndexError("invalid index")
        return self._A[item]

    def append(self, obj):
        if self._n == self._capacity:
            self._resize()

    def _resize(self, c):
        b = self._make_array(c)
        for i in range(self._n):
            b[i] = self._A[i]
        self._A = b
        self._capacity = c

    def _make_array(self, c):
        return (c * ctypes.py_object)()

    def insert(self, k, value):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        for i in range(self._n, k, -1)
            self._A[i] = self._A[i-1]
        self._A[k] = value
        self._n += 1


