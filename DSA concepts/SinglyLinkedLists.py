class SinglyNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return str(self.val)
Head = SinglyNode(1)
A = SinglyNode(3)
B = SinglyNode(4)
C = SinglyNode(7)

Head.next = A
A.next = B
B.next = C

print(Head)

print()
print("------------------------------")

#Traverse the list - O(n)

curr = Head

while curr:
    print(curr)
    curr = curr.next

print()
print("------------------------------")

#Displaying a linked list
def display(Head):
    curr = Head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print(" -> ".join(elements))
    
display(Head)

print()
print("------------------------------")

def search(head, val):
    curr = head 
    while curr:
        if val == curr:
            return True
        curr = curr.next
    return False

print(search(Head, 2))