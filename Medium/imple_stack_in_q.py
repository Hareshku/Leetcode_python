import collections
import json

class MyStack:

    def __init__(self):
        self._queue = collections.deque()

    def push(self, x):
        q = self._queue
        q.append(x)
        for _ in range(len(q) - 1):
            q.append(q.popleft())

    def pop(self):
        return self._queue.popleft()

    def top(self):
        return self._queue[0]

    def empty(self):
        return not len(self._queue)


if __name__ == "__main__":
    operations = ["MyStack", "push", "push", "top", "pop", "empty"]
    values = [[], [1], [2], [], [], []]

    obj = None
    result = []

    for op, val in zip(operations, values):
        if op == "MyStack":
            obj = MyStack()
            result.append(None)
        elif op == "push":
            obj.push(val[0])
            result.append(None)
        elif op == "pop":
            result.append(obj.pop())
        elif op == "top":
            result.append(obj.top())
        elif op == "empty":
            result.append(obj.empty())

    # Print in LeetCode-style JSON format
    print(json.dumps(result))