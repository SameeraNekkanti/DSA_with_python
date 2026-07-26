class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

head=Node(10)
second=Node(20)
third=Node(30)
fourth=Node(40)
fifth=Node(50)

head.next=second
second.next=third
third.next=fourth
fourth.next=fifth

def display(head):
    temp=head
    while temp is not None:
        print(temp.data, end="->")
        temp=temp.next

    print("None")

display(head)

def middle_node(head):
    if head is None:
        print("list is empty.")
        return

    slow=head
    fast=head

    while fast is not None and fast.next is not None:
        slow=slow.next
        fast=fast.next.next

    print("middle node: ",slow.data)

middle_node(head)