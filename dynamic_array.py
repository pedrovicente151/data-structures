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
        return  self._A[item]

    def _make_array(self, c):
        return (c * ctypes.py_object)()
