class Vector():
    def __init__(self, *args) -> None:
        self._list = list(args)

    def add(self, val: int) -> None:
        self._list.append(val)

    def remove(self, val: int) -> None:
        self._list.remove(val)
    
    @property
    def size(self) -> int:
        return len(self._list)

    def __repr__(self) -> str:
        return f"Vector{self._list}"

if __name__ == "__main__":
    v = Vector(3, 4, 5)
    v.add(6)
    print(v)
    v.remove(4)
    print(v)
    print(v.size)

