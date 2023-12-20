#function take input of integer and return number of bits that are equal to one in the binary representation of that number
def count_bits(int):
    return bin(int).count("1")

#test
print(count_bits(0))
print(count_bits(4))
print(count_bits(7))
print(count_bits(9))
print(count_bits(10))
