#using array module
from array import *
myarray_1 = array('i',[1,2,3,4,5,6,7,8,9,10])
print(myarray_1)
#using insertion 
#first element indicates te index and second element indicates te element
myarray_1.insert(10,11)
print(myarray_1)
#array traversal
def traveral_array(myarray_1):
  for i in myarray_1:
    print(i)
traveral_array(myarray_1)    
#access element
def accesselement(myarray_1,index):
  if index>=len(myarray_1):
    print("invalid index")
  else:
    print(myarray_1[index])  
accesselement(myarray_1,4)  
#searching an element
def linearsearch(myarray_1,target):
  for i in range(len(myarray_1)):
    if myarray_1[i]==target:
      print(i)
      return i
  return -1 
linearsearch(myarray_1,5) 
#deleting an element
myarray_1.remove(3) 
print(myarray_1)