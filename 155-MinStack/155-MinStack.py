# Last updated: 5/18/2025, 2:06:04 PM
class MinStack:
    # stack + min tracking stack 

    # initializes stacks using lists 
    def __init__(self):
        self.stack = []
        self.minstack = []

    # push val onto stack - append
    def push(self, val: int) -> None:
        # append min val btwn prev min + curr val
        self.minstack.append(
            # min of prefix min val & curr val 
            min(val, 
                self.minstack[-1] 
                    # check minstack has a val to check 
                    if self.minstack else val))
        self.stack.append(val)

    # removes element on top of stacks - pop
    def pop(self) -> None:
        self.minstack.pop()
        self.stack.pop()

    # gets top element of stack - read & return
    def top(self) -> int:
        return self.stack[-1]

    # find min of stack - get min stack top val 
    def getMin(self) -> int:
        return self.minstack[-1]

# Time Complexity: O(1)
# Space Complexity: O(n)

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()