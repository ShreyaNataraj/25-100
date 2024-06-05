from array import array

arrays = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

def searching(arrays, target):
    for i in range(len(arrays)):
        if arrays[i] == target:
            print(i)
            return i
    return -1

searching(arrays, 5)
