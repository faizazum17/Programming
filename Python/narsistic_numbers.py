#function that return true or false depending on whether the given number is narcissistic number in base 10
def narsissistic (n):
    #convert n to string
    n = str(n)
    #create a list of integers
    n = [int(x) for x in n]
    #create a list of n to the power of the length of n
    n = [x**len(n) for x in n]
    #return true if the sum of n is equal to the original number
    return sum(n) == int(''.join(str(x) for x in n))

#refactored
def narsissistic (n):
    return sum(int(x)**len(str(n)) for x in str(n)) == n

#test
print(narsissistic(7)) # True
print(narsissistic(371)) # True
print(narsissistic(122)) # False
print(narsissistic(4887)) # False