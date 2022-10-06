class ReverseString:
    def __init__(self) -> None:
        self.stack = []

    def push(self, data) -> None:
        """method to push data to the stack."""
        self.stack.append(data)
    
    def pop(self):
        """"method to return the latest element added in the stack."""
        last = self.stack[-1]
        self.stack.pop(-1)
        return last
    
    def reverse_string(self, inp) -> str:
        """method to reverse the string using stacks."""
        s = ReverseString()
        
        for i in range(len(inp)):
            s.push(inp[i])
        
        reverse_stack = []

        for i in range(len(inp)):
            reverse_stack.append(s.pop())
        
        reverse_string = "".join(reverse_stack)

        return reverse_string


##########################################
# Driver class
if __name__ == '__main__':
    s = ReverseString()
    
    name = 'Abin'

    print(s.reverse_string(name))