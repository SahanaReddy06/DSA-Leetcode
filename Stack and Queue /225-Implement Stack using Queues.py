from collections import deque

class MyStack:

    def __init__(self):
        self.q = deque()                      # Step 1️⃣: Initialize a single queue

    def push(self, x: int) -> None:
                                                    # Step 2️⃣: Push new element to queue
        self.q.append(x)

                                                # Step 3️⃣: Rotate the queue so new element comes to the front
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
                                                    # Step 4️⃣: Pop the front element (top of stack)
        return self.q.popleft()

    def top(self) -> int:
                                              # Step 5️⃣: Peek the front element (top of stack)
        return self.q[0]

    def empty(self) -> bool:
                                            # Step 6️⃣: Check if stack is empty
        return len(self.q) == 0
