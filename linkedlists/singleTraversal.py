class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

head=Node(10)
second=Node(20)
third=Node(30)
fourth=Node(40)

head.next=second
second.next=third
third.next=fourth

def display(head):
    temp=head
    while temp is not None:
        print(temp.data, end="->")
        temp=temp.next

    print("None")

display(head)

def second_last(head):
    if head is None or head.next is None:
        print("second element does not exist.")
        return

    temp=head

    while temp.next.next is not None:
        temp=temp.next

    print("second last element: ",temp.data)

second_last(head)