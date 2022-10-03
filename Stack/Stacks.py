class Stack:
    def __init__(self, limit = 10) -> None:
        self.stack = []
        self.limit = limit
    
    def push(self, data):
        self.stack.append(data)
    
    def pop(self):
        '''it returns the top most data in the stack.'''
        if self.stack == []:
            raise Exception('Stack Underflow: The stack is empty!')
        return self.stack[0]

    def print_stack(self):
        '''prints the stack with the last element at the top, and the first element at the bottom.'''
        for data in range(len(self.stack) - 1, -1, -1):
            print(self.stack[data])
        
    def length(self) -> int:
        '''returns the length of the stack.'''
        return len(self.stack)
    
    def is_even(self) -> bool:
        if self.length() % 2 == 0:
            return True
        else:
            return False

############################################################
# The driver class
if __name__ == '__main__':
    s = Stack()
    '''s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
'''
    s.pop()