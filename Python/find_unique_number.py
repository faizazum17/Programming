#find the uniqe number in array
def find_uniq(arr):
    #your code here
    arr.sort()
    if arr[0] == arr[1]:
        return arr[-1]
    else:
        return arr[0]
    
#test
print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))
print(find_uniq([ 0, 0, 0.55, 0, 0 ]))
