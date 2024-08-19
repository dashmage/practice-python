# Queue implementation using a Linked List

from dataclasses import dataclass
from typing import Self


class LinkedQueue:
    @dataclass
    class _Node:
        __slots__ = "data", "next"
        data: int | None
        next: Self | None

    def __init__(self) -> None:
        self._front: self._Node | None = None
        self._back: self._Node | None = None
        self._size: int = 0

    def __len__(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    def first(self) -> int:
        return self._head.data

    def enqueue(self, val: int) -> None:
        new_node = self._Node(val, None)
        if self.is_empty():
            self._front = new_node
        else:
            self._back.next = new_node
        self._back = new_node
        self._size += 1

    def dequeue(self) -> int:
        if self.is_empty():
            raise RuntimeError("Queue is empty")
        dequeue_val = self._front.data
        self._front = self._front.next
        self._size -= 1
        if self.is_empty():
            self._back = None
        return dequeue_val

    def __repr__(self) -> str:
        if self.is_empty():
            return "Empty Queue"
        ptr = self._front
        result = []
        while ptr is not None:
            result.append(str(ptr.data))
            ptr = ptr.next
        return " <-> ".join(result)


q = LinkedQueue()
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print(q)
