'SRC1 - linked list module'
class Node:
  'Node class for linked list'
  def __init__(self,data :int,ptr :int) -> None:
    self.data = data
    self.ptr = ptr
  #end procedure

  def __repr__(self) -> str:
      return f'(Data: {self.data}; Pointer: {self.ptr})'
  #end function
#end class

class LinkedList:
  'Linked list class'
  def __init__(self,size) -> None:
    self.sp = -1
    self.nf = 0
    self.container = [Node(None,-1)]
    while size > 1:
      self.container.insert(0,Node(None,size-1))
      size -= 1
    #end while
  #end procedure (constructor)

  def isFull(self):
      if self.nf == -1: return True
      else: return False

  def add(self,item):
      if not (self.isFull()):
          if self.container[self.sp].data==None:
              self.sp = 0
              self.container[self.sp].data = item
              self.nf = self.container[self.nf].ptr
              
          else:
            index = self.sp
            new = self.nf
            self.nf = self.container[self.nf].ptr

            if self.container[self.sp].data > item:
              self.container[new].data = item
              self.container[self.sp].ptr = self.container[new].ptr
              self.container[new].ptr = self.sp
              self.sp = new

            else:

              peek = self.container[self.container[index].ptr].data
              
              while peek != None and peek < item:
                index = self.container[index].ptr
                peek = self.container[self.container[index].ptr].data

              self.container[new].data = item
              if peek != None:
                self.container[new].ptr = self.container[index].ptr
                self.container[index].ptr = new
                                                      
              
  def __repr__(self) -> str:
    output_str = f'(Start Pointer: {self.sp}; Next free: {self.nf})\n'
    for node in self.container:
      output_str += node.__repr__() + '\n'
    #next node
    return output_str
  #end function

  

#end class
    


if __name__ == "__main__":
  my_list = LinkedList(5)
  print(my_list)
  my_list.add(3)
  print(my_list)
  my_list.add(1)
  print(my_list)
  my_list.add(4)
  print(my_list)
  my_list.add(2)
  print(my_list)


  #3,1,4,2,5
