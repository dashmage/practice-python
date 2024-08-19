# Singly linked list

from dataclasses import dataclass
from typing import Self


class EmptyListError(Exception): ...


@dataclass
class SLLNode:
    data: int | None = None
    next: Self | None = None


class SLL:
    def __init__(self):
        self._head: SLLNode | None = None
        self._size: int = 0

    def size(self) -> int:
        return self._size

    def empty(self) -> bool:
        return self._size == 0

    def front(self) -> int:
        if self.empty():
            raise EmptyListError
        return self._head.data

    def back(self) -> int:
        if self.empty():
            raise EmptyListError
        ptr = self._head
        while ptr.next is not None:
            ptr = ptr.next
        return ptr.data

    def value_at(self, index: int) -> int:
        """Return value of nth item starting from 0."""
        if index < 0:
            raise ValueError("Index can't be less than 0")
        ptr = self._head
        if self.empty():
            raise EmptyListError("Can't lookup value on empty list")
        for i in range(index):
            if ptr.next is None:
                raise ValueError("Invalid index")
            ptr = ptr.next
        return ptr.data

    def push_front(self, new_data: int) -> None:
        new_node = SLLNode(data=new_data, next=self._head)
        self._head = new_node
        self._size += 1

    def pop_front(self) -> int | None:
        # LL is empty
        if self.empty():
            raise EmptyListError("Can't pop from empty list")
        popped = self._head.data
        self._head = self._head.next
        self._size -= 1
        return popped

    def push_back(self, new_data: int) -> None:
        new_node = SLLNode(data=new_data)
        ptr = self._head
        while ptr.next is not None:
            ptr = ptr.next
        ptr.next = new_node
        self._size += 1

    def pop_back(self) -> int:
        ptr = self._head
        if self.empty():
            raise EmptyListError("Can't pop from empty list")
        if self._size == 1:
            popped = self.pop_front()
        else:
            while ptr.next.next is not None:
                ptr = ptr.next
            popped = ptr.next.data
            ptr.next = None
            self._size -= 1
        return popped

    def insert(self, index: int, value: int):
        if index >= self._size:
            raise ValueError("Invalid index greater than size")

        if index < 0:
            raise ValueError("Index can't be less than 0")
        elif index == 0:
            self.push_front(value)
        else:
            ptr = self._head
            for i in range(index - 1):
                # we don't go off the end since we already check that index < size
                ptr = ptr.next
            self._size += 1
            new_node = SLLNode(data=value, next=ptr.next)
            ptr.next = new_node

    def delete(self, index: int) -> int:
        """Delete node at specified index."""
        if index < 0:
            raise ValueError("Index can't be less than 0")
        if self.empty():
            raise EmptyListError("Deleting on empty list")

        if index == 0:
            deleted = self.pop_front()
        # if index > 0 and there's only one element
        elif self._size == 1:
            raise ValueError("Invalid index")
        else:
            ptr = self._head
            for i in range(index - 1):
                if ptr.next.next is None:
                    raise ValueError("Invalid index")
                ptr = ptr.next
            deleted = ptr.next.data
            ptr.next = ptr.next.next
            self._size -= 1
        return deleted

    def __repr__(self) -> str:
        if self.empty():
            return "Empty"
        ptr = self._head
        values = []
        while ptr is not None:
            values.append(str(ptr.data))
            ptr = ptr.next
        return " -> ".join(values)


if __name__ == "__main__":
    s = SLL()
    try:
        s.value_at(2)
    except EmptyListError as e:
        print(f"Caught expected exception: {e.__class__.__name__}, {e}")
    assert s.size() == 0
    try:
        s.pop_front()
    except EmptyListError as e:
        print(f"Caught expected exception: {e.__class__.__name__}, {e}")
    s.push_front(1)
    s.push_front(3)
    s.push_front(7)
    s.insert(1, 5)
    assert s.value_at(2) == 3
    try:
        s.value_at(5)
    except ValueError as e:
        print(f"Caught expected exception: {e.__class__.__name__}, {e}")
    assert s.__repr__() == "7 -> 5 -> 3 -> 1"
    assert s.size() == 4
    try:
        s.insert(4, 10)
    except ValueError as e:
        print(f"Caught expected exception: {e.__class__.__name__}, {e}")
    s.pop_front()
    assert s.__repr__() == "5 -> 3 -> 1"
    assert s.size() == 3
    s.push_back(11)
    s.push_back(13)
    assert s.__repr__() == "5 -> 3 -> 1 -> 11 -> 13"
    assert s.size() == 5
    s.pop_back()
    assert s.__repr__() == "5 -> 3 -> 1 -> 11"
    assert s.size() == 4
    assert s.front() == 5
    assert s.back() == 11
    assert s.delete(2) == 1
    assert s.delete(0) == 5
    assert s.__repr__() == "3 -> 11"
    assert s.size() == 2
    print(f"{s = }")
    print(f"{s.size() = }")
