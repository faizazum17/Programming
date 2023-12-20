#find the one that appears an odd number of times
def find_it(arr):
    #your code here
    for i in arr:
        if arr.count(i) % 2 != 0:
            return i
    return None

#test
print(find_it([1,1,2,-2,5,2,4,4,-1,-2,5]))
print(find_it([20,1,1,2,2,3,3,5,5,4,20,4,5]))
print(find_it([10]))
print(find_it([1,1,1,1,1,1,10,1,1,1,1]))
print(find_it([5,4,3,2,1,5,4,3,2,10,10]))