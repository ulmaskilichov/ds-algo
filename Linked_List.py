class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    
    def __repr__(self) -> str:
        return self.val

class LinkedList:
    def __init__(self, head):
        self.head = head
    
    def __repr__(self) -> str:
        current = self.head
        ans = []
        while current:
            ans.append(current.val)
            current = current.next
        ans.append('None')
        return '->'.join(ans)
    
def find(node:LinkedList, element:str) -> bool:
    current = node
    while current != None:
        if current.val==element:
            return True
        current = current.next
    return False
def insert(head, newnode, index):
    cur = head
    i = 0
    if index == 0:
        newnode.next = cur
        cur = newnode
    else:
        while i < index - 1:
            cur = cur.next
            i += 1
        newnode.next=cur.next
        cur.next = newnode
def remove(head, index):
    i = 0
    if index == 0:
        head=head.next
    else:
        while i < index -1:
            head = head.next
            i += 1
        head.next = head.next.next
        
a = Node('1')
b = Node('2')
c = Node('3')
a.next=b
b.next=c

head = LinkedList(a)

print(find(a, '5'))
print(head)
newnode = Node('0')
insert(a, newnode, 2)
print(head)