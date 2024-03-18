''' write a program using opps conpect to implement linked list write the method to
1.Display the list of element in the list.
2.insert a node at any possition.
3.Delete a node at any possition.
'''

class N:
    #to take the elements as input
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None

class LList:

    #to create the linkedlist
   def __init__(self):
      self.headval = None

    #to traverse the linkedlist
   def element(self):
      val = self.headval
      print('The elements are')
      while val is not None:
         print(val.dataval,end=' ')
         val = val.nextval

    #to insert an element into the linked list
   def insertele(self,data=None):
       newval=N(data)
       if self.headval is None:
         self.headval = newval
         return 

       else:
           last=self.headval
           while(last.nextval):
               last = last.nextval
           last.nextval=newval
       
list = LList()
ele1=N('1')
list.headval=ele1

ele2 = N('2')
ele1.nextval = ele2

ele3 = N('3')
ele2.nextval = ele3

ele4 = N(input('Enter an element'))
list.insertele(ele4)

ele5 = N(input('Enter an element'))
list.insertele(ele5)

list.element()
