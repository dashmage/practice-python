from dataclasses import dataclass
from typing import Self


class LinkedStack:
    # Nested lightweight, non-public Node class
    @dataclass
    class _Node:
        __slots__ = "data", "next"
        data: int | None
        next: Self | None

    def __init__(self):
        self._head: self._Node | None = None
        self._size: int = 0

    def __len__(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    def push(self, val: int) -> None:
        self._head = self._Node(val, self._head)
        self._size += 1

    def top(self) -> int:
        if self.is_empty():
            raise RuntimeError("Stack is empty")
        return self._head.data

    def pop(self):
        if self.is_empty():
            raise RuntimeError("Stack is empty")
        pop_data = self._head.data
        self._head = self._head.next
        self._size -= 1
        return pop_data
