import ctypes  # provides low-level arrays


"""
NOTES
-----
size     -> number of elements in array
capacity -> storage provisioned for array

Steps to grow the array when it's full
* Allocate a new array B with larger capacity
* Set B[i] = A[i], for i=0, 1, 2, ... (size-1) where size is the current number of items
* Set A = B
* Insert new element into the new array

In this implementation, we will double the capacity each time the array is full.
"""

class DynamicArray:
    """A dynamic array class similar to a Python list."""

    def __init__(self):
        """Create an empty array."""
        self._size = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def __len__(self):
        """Return number of elements stored in the array."""
        return self._size

    def __getitem__(self, k):
        """Return element at index k."""
        if not 0 <= k <= self._size:
            raise IndexError("invalid index")
        return self._A[k]

    def append(self, obj):
        """Add object to end of the array."""
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._size] = obj
        self._size += 1

    def _resize(self, c):
        """Resize internal array to capacity c."""
        B = self._make_array(c)
        for k in range(self._size):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def _make_array(self, c):
        """Return new array with capacity c."""
        return (c * ctypes.py_object)()

    def __repr__(self):
        r = ""
        r += "["
        for i in range(self._size):
            r += str(self._A[i])
            if i != self._size - 1:
                r += ", "
        r += "]"
        return r
