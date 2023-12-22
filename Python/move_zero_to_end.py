#function that take an array and move zero to end
def move_zero_to_end(arr):
    #your code here
    #create a list of tuples
    arr = [(x, 0) if x != 0 else (x, 1) for x in arr]
    #sort the list of tuples
    arr.sort(key=lambda x: x[1])
    #create a list of integers
    arr = [x[0] for x in arr]
    return arr

#refactored
def move_zero_to_end(arr):
    return sorted(arr, key=lambda x: x==0)    

#test  
print(move_zero_to_end([1,2,0,1,0,1,0,3,0,1])) # [1, 1, 1, 1, 2, 3, 0, 0, 0, 0]