class MyQueue:

    def __init__(self):
        self.stack1 = []  #  Stack for push operations
        self.stack2 = []  #  Stack for pop/peek operations

    def push(self, x: int) -> None:
                                            #  Always push new element to stack1
        self.stack1.append(x)
      

    def pop(self) -> int:
                                                #  Ensure stack2 has elements to pop from
        if not self.stack2:
            while self.stack1:                  # Move all elements from stack1 to stack2
                self.stack2.append(self.stack1.pop())
                                                # Pop from stack2 → front of queue
        return self.stack2.pop()
      

    def peek(self) -> int:
                                              # Ensure stack2 has elements to peek
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
                                              #  Peek top of stack2 → front of queue
        return self.stack2[-1]
      

    def empty(self) -> bool:
                                                      #  Queue is empty only if both stacks are empty
        return not self.stack1 and not self.stack2
