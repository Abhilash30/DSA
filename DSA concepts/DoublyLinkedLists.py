class Doublynode:
    def __init__(self, val, prev = None, next = None):
        self.val = val 
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.val)
    
head = tail = Doublynode(1)



#O(n) to display
def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print(" <-> ".join(elements))

display(head)

# Insert at the beginning O(1)
def insert_at_beg(head, tail, val):
    new_node = Doublynode(val, next= head)
    head.prev = new_node
    return new_node, tail
head, tail = insert_at_beg(head, tail, 3)
display(head)

def insert_at_end(head, tail,val):
    new_node = Doublynode(val, prev=tail)
    tail.next = new_node
    return head, new_node

head, tail = insert_at_end(head, tail, 7)
display(head)