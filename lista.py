class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LancoltLista:
    head=None
    def appendForward(self,elem):
        new=Node(elem)
        new.next=self.head
        self.head=new
    def appendBack(self,elem):
        new_back=Node(elem)
        if self.head==None:
            self.head=new_back
        else:
            current_item=self.head
            while current_item.next!=None:
                current_item=current_item.next
            current_item.next=new_back
    def delete(self,elem):
        tmp=self.head
        previous=None
        while tmp!=None:
            if tmp.data==elem:
                if previous==None:
                    self.head=self.head.next
                else:
                    previous.next=tmp.next
            previous=tmp
            tmp=tmp.next
    def write(self):
        tmp=self.head
        print("A lista elemei:")
        while tmp!=None:
            print(tmp.data,'->',end="")
            tmp=tmp.next
        print("None")
    def append(self,data,data_from):
        new_append=Node(data)
        if self.head==None:
            self.head=new_append
        else:
            tmp=self.head
            a=False
            while tmp!=None:
                if tmp.data==data_from:
                    b=tmp.next
                    tmp.next=new_append
                    new_append=tmp
                    tmp.next.next=b

                    a=True

                if a==False:
                    tmp=tmp.next
                else:
                    break


s=LancoltLista()
s.appendForward(23)
s.appendForward(42)
s.appendBack(11)
s.appendBack(77)
s.append(24,11)
s.append(55,77)
s.append(12,42)
s.write()
