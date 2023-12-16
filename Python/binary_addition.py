#inplement funtion that adds two  numbers together and return sum in binary
#example(input1n input2, --> output)
def add_binary(a, b):
    #your code here
    return bin(a + b)[2:]

#test cases
print(add_binary(1, 1)) #10
print(add_binary(0, 1)) #1
print(add_binary(1, 0)) #1
print(add_binary(2, 2)) #100