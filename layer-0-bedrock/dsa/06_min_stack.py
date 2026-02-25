class MinStack:
    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.mins or val <= self.mins[-1]:
            self.mins.append(val)

    def pop(self) -> int:
        if not self.stack:
            raise IndexError("pop from empty stack")
        val = self.stack.pop()
        if self.mins and val == self.mins[-1]:
            self.mins.pop()
        return val

    def top(self) -> int:
        if not self.stack:
            raise IndexError("top from empty stack")
        return self.stack[-1]

    def get_min(self) -> int:
        if not self.mins:
            raise IndexError("min from empty stack")
        return self.mins[-1]

if __name__ == "__main__":
    ms = MinStack()
    ms.push(-2); ms.push(0); ms.push(-3)
    assert ms.get_min() == -3
    ms.pop()
    assert ms.top() == 0
    assert ms.get_min() == -2
    print("ok")
