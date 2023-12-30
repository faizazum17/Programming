#function that return the square of each digit of a number and concat them
'''def square_digit (n):
    #convert n to string
    n = str(n)
    #create a list of integers
    n = [int(x) for x in n]
    #create a list of n to the power of the length of n
    n = [x**2 for x in n]
    #return true if the sum of n is equal to the original number
    return int(''.join(str(x) for x in n))'''

def square_digit (n):
    return int(''.join(str(int(x)**2) for x in str(n)))

#test
print(square_digit(9119)) # 811181
print(square_digit(0)) # 0
print(square_digit(1111)) # 1111
print(square_digit(1234321)) # 14916941