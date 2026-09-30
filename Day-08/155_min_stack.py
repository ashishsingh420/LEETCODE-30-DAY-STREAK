class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val):
        self.stack.append(val)

        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self):
        val = self.stack.pop()

        if val == self.minStack[-1]:
            self.minStack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minStack[-1]


# Testing

minStack = MinStack()

minStack.push(-2)
minStack.push(0)
minStack.push(-3)

print(minStack.getMin())

minStack.pop()

print(minStack.top())
print(minStack.getMin())



# Leetcode Problem 155: Min Stack

# class MinStack:

#     def __init__(self):
#         self.stack = []
#         self.minStack = []

#     def push(self, val: int) -> None:

#         self.stack.append(val)

#         if not self.minStack or val <= self.minStack[-1]:
#             self.minStack.append(val)

#     def pop(self) -> None:

#         val = self.stack.pop()

#         if val == self.minStack[-1]:
#             self.minStack.pop()

#     def top(self) -> int:

#         return self.stack[-1]

#     def getMin(self) -> int:

#         return self.minStack[-1]