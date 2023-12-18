#function that take a list of non negative integer and string and return a new list with the string filtered out
def filter_list(arr):
    for i in arr:
        if (type(i)) == str:
            arr.remove(i)
    return arr

#refactored
def filter_list2(arr):
    return [i for i in arr if type(i) != str]

print(filter_list([1,2,'a','b'])) #[1,2]