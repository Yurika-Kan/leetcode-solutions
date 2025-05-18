# Last updated: 5/18/2025, 1:33:54 PM
class MinStack:
    # initializes stacks 
    def __init__(self):
        self.stack = []
        self.minstack = []

    # pushes element val onto stack - append
    def push(self, val: int) -> None:
        self.minstack.append(
            # min of prefix min val & curr val 
            min(val, 
                self.minstack[-1] 
                    # check minstack has a val to check 
                    if self.minstack else val))
        self.stack.append(val)

    # removes element on top of stack - pop
    def pop(self) -> None:
        self.minstack.pop()
        self.stack.pop()

    # gets top element of stack - read
    def top(self) -> int:
        return self.stack[-1]

    # find min of stack 
    def getMin(self) -> int:
        return self.minstack[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()