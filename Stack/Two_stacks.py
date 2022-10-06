class TwoStacks:
    def __init__(self, size = 10) -> None:
        self.size = size
        self.stack = [None] * size
        self.p1 = 0
        self.p2 = -1

    """def push1(self, data) -> None:
        '''we have to reserve the first half of the array for stack1.
        we will start pushing data to it from index 0 uptil size//2.'''
        if not self.arr[(self.size // 2) - 1]:
            self.arr.append(data)
        else:
            raise Exception('Stack1 overflow: Stack1 is full.')
"""

    def push1(self, data) -> None:
        if self.stack[self.p1] is None:
            self.stack[self.p1] = data
            self.p1 += 1
        else:
            raise Exception('Stack1 Overflow!')
        
    def push2(self, data) -> None:
        if self.stack[self.p2] is None:
            self.stack[self.p2] = data
            self.p2 -= 1
        else:
            self.p2 += 1
            raise Exception('Stack2 Overflow!')
    
    def pop1(self):
        if self.p1 <= 0:
            raise Exception('Stack1 Underflow!')
        self.p1 -= 1
        res = self.stack[self.p1]
        self.stack[self.p1] = None
        return res
    
    def pop2(self):
        if self.p2 >= -1:
            raise Exception('Stack2 Underflow!')
        self.p2 += 1
        res = self.stack[self.p2]
        self.stack[self.p2] = None
        return res
    
    def print_stacks(self) -> list:
        for index in range(len(self.stack) - 1, -1, -1):
            print(self.stack[index])

##############################################
# The driver function

if __name__ == '__main__':
    s = TwoStacks(6)
    s.push1(1)
    s.push2(2)
    s.push1(3)
    s.push2(4)
    s.push1(5)
    s.push2(6)

    s.print_stacks()
    print()

    #print(s.pop1())
    #s.print_stacks()
    s.pop1()
    s.print_stacks()
    print()
    s.pop1()
    s.print_stacks()
    print()
    s.pop1()
    s.print_stacks()
    print()
    s.pop1()

    """Output:
    2
    4
    6
    5
    3
    1

    2
    4
    6
    None
    3
    1

    2
    4
    6
    None
    None
    1

    2
    4
    6
    None
    None
    None


    Exception: Stack1 Underflow!
    """
        