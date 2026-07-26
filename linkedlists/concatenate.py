class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

def concatenate(L,M):
    if L is None:
        return M
    
    temp=L
    while temp.next is not None:
        temp=temp.next

    temp.next=M
    return L

def display(head):
    temp=head
    while temp is not None:
        print(temp.data, end="->")
        temp=temp.next

    print("None")

head1=Node(10)
second1=Node(20)
third1=Node(30)
head1.next=second1
second1.next=third1

head2=Node(50)
second2=Node(60)
third2=Node(70)
head2.next=second2
second2.next=third2

display(concatenate(head1, head2))