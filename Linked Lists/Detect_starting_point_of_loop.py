from Node import Node
from Detect_loop_in_linked_list import LinkedList

class DetectStartingPoint(LinkedList):
    def __init__(self) -> None:
        super().__init__()                  # inheriting the parent's constructor

    def detect_starting_point(self) -> Node:
        if self.detect_loop():
            current = self.head
            s = set()
            while(current):
                if current in s:
                    return current
                s.add(current)
                current = current.next
        return None

#########################3

# Driver class
if __name__ == '__main__':
    ll = DetectStartingPoint()
    for i in range(6):
        ll.push(i)
    
    ll.head.next.next.next = ll.head           # creating a loop   

    print(ll.detect_starting_point())

    """output:
    Loop present
    <Node.Node object at 0x0000021BA3723D90>"""
    