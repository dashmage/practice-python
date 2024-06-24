class Empty(Exception):
    pass


class ArrayQueue:
    DEFAULT_CAPACITY = 4

    def __init__(self):
        """Initialize empty queue."""
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """Return number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return whether the queue is empty."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue.

        Raises Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._data[self._front]

    def _resize(self, capacity):
        """Resize internal list to new capacity."""
        new = [None] * capacity
        for i in range(self._size):
            next = (self._front + i) % len(self._data)
            new[i] = self._data[next]
        self._data = new
        self._front = 0

    def enqueue(self, e):
        """Add element e to the front of the queue."""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        pos = (self._front + self._size) % len(self._data)
        self._data[pos] = e
        self._size += 1

    def dequeue(self):
        """Remove and return element from the end of the queue.

        Raises Empty exception if queue is empty.
        """
        if self.is_empty():
            raise Empty("Queue is empty")
        # reduce array to half the size whenever number of elements falls below a
        # fourth of capacity
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        e = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return e


if __name__ == "__main__":
    Q = ArrayQueue()
    assert Q.is_empty() == True
    Q.enqueue(5)
    Q.enqueue(7)
    Q.enqueue(9)
    assert Q._data == [5, 7, 9, None]
    assert Q._size == 3
    assert Q._front == 0
    e = Q.dequeue()
    assert e == 5
    e = Q.dequeue()
    assert e == 7
    assert Q._data == [None, None, 9, None]
    assert Q._size == 1
    assert Q._front == 2
    Q.enqueue(11)
    Q.enqueue(13)
    Q.enqueue(15)
    assert Q._data == [13, 15, 9, 11]
    assert Q._size == 4
    assert Q._front == 2
    Q.enqueue(17)
    assert Q._data == [9, 11, 13, 15, 17, None, None, None]
    assert Q._size == 5
    assert Q._front == 0

    print("Tests Pass")
