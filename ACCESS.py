import array
arrayss = array.array('i', [1,2,3,4,5,6,7,8,9])
def accesselement(array,index):
  if index>=len(array):
    print("Index out of the range")
  else:
    print(array[index])
accesselement(arrayss,6)      