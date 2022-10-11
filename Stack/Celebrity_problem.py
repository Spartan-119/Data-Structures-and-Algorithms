from Stacks import Stack

class Celebrity(Stack):
    """
    ALGORITHM (using stacks):

    1. Create a stack and push all ids in it.
    2. Run a loop while there are more than one element in the stack
    and in each iteration do the following:
        2.1. Pop two elements from the stack. Let these elements be ‘id1’ and ‘id2’.
        2.2. If the person with ‘id1’ knows the person with ‘id2,’ i.e. ‘knows(id1, id2)’
        return true, then the person with ‘id1’ cannot be a celebrity, so push ‘id2’ in the stack.
        2.3. Otherwise, if the person with ‘id1’ doesn't know the person with ‘id2,’ i.e.
        knows(id1, id2) return false, then the person with ‘id2’ cannot be a celebrity,
        so push ‘id1’ in the stack.
    3. Only one id remains in the stack; you need to check whether the person having
    this id is a celebrity or not, this can be done by running two loops.
    One checks whether this person is known to everyone or not, and another loop
    will check whether this person knows anyone or not.
    4. If this person is a celebrity, return his id; otherwise, return -1.
    """
    def __init__(self) -> None:
        super().__init__()
    
    def find_celebrity(self, s, matrix) -> int:
        n = s.length()
        while s.length() > 1:
            id1 = s.pop()
            id2 = s.pop()

            if matrix[id1][id2]:
                # id1 cant't be a celeb
                # id2 could be a potential celeb, so push it in the stack.
                s.push(id2)
            else:
                # id2 can't be a celeb, because there's at least one person
                # who doesn't recognize them.
                # id1 could be a potential celeb, so push it in the stack.
                s.push(id1)

        id = s.pop()                    # id holds whichever ID is left in the stack.

        for i in range(n):
            if matrix[id][i]:
                return -1
        
        for i in range(n):
            if not matrix[i][id]:
                if matrix[id][id]:
                    continue
                return 0

        return id

################################
# Driver class
if __name__ == '__main__':
    # Person with 2 is celebrity
    MATRIX = [ [ 0, 0, 1, 0 ],
           [ 0, 0, 1, 0 ],
           [ 0, 0, 0, 0 ],
           [ 0, 0, 1, 0 ] ]

    c = Celebrity()

    s = Stack()
    s.push(0)
    s.push(1)
    s.push(2)
    s.push(3)
    
    if c.find_celebrity(s, MATRIX) == -1:
        print('no celebrity')
    else:
        print('The celebrity is at the index:', c.find_celebrity(s, MATRIX))