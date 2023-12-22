#function that decide to attribute a "weight" to numbers. The weight of a number will be from now on the sum of its digits.
def order_weight(arr):
    # your code
    #split the string into a list of strings
    arr = arr.split()
    #create a list of tuples
    arr = [(int(x), sum(int(i) for i in x)) for x in arr]
    #sort the list of tuples
    arr.sort(key=lambda x: (x[1], x[0]))
    #create a list of strings
    arr = [str(x[0]) for x in arr]
    #join the list of strings into one string
    arr = ' '.join(arr)
    return arr

#refactored
def order_weight(arr):
    return ' '.join(sorted(arr.split(), key=lambda x: (sum(int(i) for i in x), x)))


#test
print(order_weight("103 123 4444 99 2000")) # "2000 103 123 4444 99"
print(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123")) # "11 11 2000 10003 22 123 1234000 44444444 9999"

    