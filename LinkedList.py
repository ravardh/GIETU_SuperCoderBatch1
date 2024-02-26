class Node:
    def _init_(self,data):
        self.data=data
        self.next=None
    def ins_at_first(self,head):
        self.next=head
        head=self
        return head
    def ins_at_end(self,head):
        cur=head
        while cur.next!=None:
            continue
        return cur
    def ins_in_bet(self,pos,head):
        cur=head
        for i in range(1,pos):
            before=cur
            cur=cur.next
        return before
    def print_list(self):
        cur=self
        while cur:
            print(cur.data)
            cur=cur.next
    def del_first_node(self):
        cur=self
        head=self.next
        cur.next=None
        return head
    def del_last_node(self):
        cur=self
        while cur.next.next:
            cur=cur.next
        return cur
    def del_bet_nodes(self,pos):
        cur=self
        for i in range(1,pos-1):
            cur=cur.next
        return cur

ch=True
head=None
while(ch==True):
    print("Enter the operation to perform:\n")
    oper=int(input())
    #1-insertion in between,2-insertion at beginning,3-insertion at end
    #4-deletion of node in between two nodes,5-delete first node,6-delete last node
    #7-print the linked list
    match oper:
        case 1:
            data=int(input("Enter the data node:\n"))
            pos=int(input("Enter the position where the node has to be inserted b/w 2nd node and last node:\n"))
            newnode=Node(data)
            before=newnode.ins_in_bet(pos,head)#node before the newnode
            temp=before.next
            before.next=newnode
            newnode.next=temp
        case 2:
            data=int(input("Enter the data of the first node:\n"))
            newnode=Node(data)
            head=newnode.ins_at_first(head)
        case 3:
            data=int(input("Enter the data of the last node:\n"))
            newnode=Node(data)
            prev_node=newnode.ins_at_end(head)#returns the present list's last node
            prev_node.next=newnode#prev_node is newnode's previous node
            newnode.next=None
        case 4:
            pos=int(input("Enter the position of the node to be deleted for pos:[2,last node)):\n"))
            prev_node=head.del_bet_nodes(pos)
            temp=prev_node.next.next
            prev_node.next=temp
        case 5:
            if(head!=None):
              temp=head.del_first_node()
              head=temp
            else:
              print("Empty List")
        case 6:
            second_last_node=head.del_last_node()
            second_last_node.next=None
        case 7:
            if head!=None:
                head.print_list() 
            else:
                print("Empty list")
        case None:
            pass
           
    print("Do you wanna continue:\n")
    ch=input("Enter the choice:t or f")
    if(ch=='t'):
        ch=True
    elif(ch=='f'):
        ch=False
