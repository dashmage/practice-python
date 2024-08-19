# Doubly linked list

from dataclasses import dataclass
from typing import Self


class DLL:
    @dataclass
    class _Node:
        __slots__ = "data", "next", "prev"
        data: int | None
        next: Self | None
        prev: Self | None

    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header.next = self._trailer
        self._trailer.prev = self._header
        self._size: int = 0

    def size(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    def front(self) -> int:
        if self.is_empty():
            raise RuntimeError("Linked list is empty")
        return self._header.next.data

    def back(self) -> int:
        if self.is_empty():
            raise RuntimeError("Linked list is empty")
        return self._trailer.prev.data

    def insert_between(
        self, value: int, predecessor: _Node | None, successor: _Node | None
    ) -> _Node:
        """Add node between two existing nodes and return the newly created node."""
        new_node = self._Node(value, successor, predecessor)
        predecessor.next = new_node
        successor.prev = new_node
        self._size += 1
        return new_node

    def delete_between(self, node: _Node) -> int:
        """Delete non-sentinel node from the list and return its data."""
        predecessor = node.prev
        successor = node.next
        predecessor.next = successor
        successor.prev = predecessor
        self._size -= 1
        deleted_value = node.data
        node.prev = node.next = node.data = None
        return deleted_value

    def insert_front(self, value: int) -> None:
        self.insert_between(value, self._header, self._header.next)

    def insert_back(self, value: int) -> None:
        self.insert_between(value, self._trailer.prev, self._trailer)

    def delete_front(self) -> int:
        if self.is_empty():
            raise RuntimeError("Can't delete from an empty list")
        return self.delete_between(self._header.next)

    def delete_back(self) -> int:
        if self.is_empty():
            raise RuntimeError("Can't delete from an empty list")
        return self.delete_between(self._trailer.prev)

    def reverse(self) -> None:
        if self.is_empty():
            raise RuntimeError("Can't reverse empty list")
        current = self._header.next
        while current is not self._trailer:
            current.prev, current.next = current.next, current.prev
            current = current.prev
        self._header, self._trailer = self._trailer, self._header
        self._header.next, self._trailer.prev = self._header.prev, self._trailer.next
        self._header.prev = self._trailer.next = None

    def __repr__(self) -> str:
        if self.is_empty():
            return "Empty"
        ptr = self._header.next
        result = []
        while ptr is not self._trailer:
            result.append(str(ptr.data))
            ptr = ptr.next
        return " <-> ".join(result)


if __name__ == "__main__":
    d = DLL()
    d.insert_back(5)
    d.insert_front(4)
    d.insert_back(6)
    assert d.__repr__() == "4 <-> 5 <-> 6"
    assert d.size() == 3
    d.reverse()
    assert d.__repr__() == "6 <-> 5 <-> 4"
