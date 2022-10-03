from Stacks import Stack

class MiddleElement(Stack):
    def __init__(self) -> None:
        super().__init__()
    
    def find_middle(self):
        n = self.length()
        '''returns the middle element(s) of the stack.'''
        if self.is_even():
            return (self.stack[(n // 2) - 1], self.stack[n // 2])           # would return the two middle values if n is even.
        else:
            return self.stack[n // 2]

############################################################
# The driver class
if __name__ == '__main__':
    s = MiddleElement()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    s.push(6)

    print(s.find_middle())