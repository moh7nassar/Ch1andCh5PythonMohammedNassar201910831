class Node:
   def __init__(self, dataval=None):
       self.dataval=dataval
       self.nextval=None

class SLinkedList:
      def __init__(self):
          self.headval=None

list1=SLinkedList()
list2.headval=Node("Mon")
e2=Node("Tue")
e3=Node("Wed")

list.headval.nextval=e2
e2.nextval=e3
