def CheckSymbolBalance(input):
    symbolStack = [] # creating an empty stack to check
    balanced = False # flag
    opening_symbols = ['(', '[', '{', '<']
    closing_symbols = [')', ']', '}', '>']

    for symbol in input:
        if symbol in opening_symbols:
            symbolStack.append(symbol)
        else:
            # if the current sumbol is not in the opening bracket
            # then it must be in the closing bracket. In such case
            # the stack must be empty after the operation. It CANNOT 
            # have any symbol left in it.
            if not symbolStack:
                return False

            current_symbol = symbolStack.pop()
            
            if current_symbol == '(':
                if symbol != ')':
                    return False
                
            if current_symbol == '[':
                if symbol != ']':
                    return False
                            
            if current_symbol == '{':
                if symbol != '}':
                    return False
                
            if current_symbol == '<':
                if symbol != '>':
                    return False
                
    
    # if the stack is not empty then return False, else true
    if symbolStack:
        return False
    return True

# checking
input1 = '()([])'
input2 = '()('

print(CheckSymbolBalance(input1))
print(CheckSymbolBalance(input2))