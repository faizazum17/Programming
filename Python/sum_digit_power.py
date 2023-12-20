#function that collect numbers and outputs list of the sorted numbers in the range that fulfill the property described below
def sum_dig_pow(a, b):
    #your code here
    return [i for i in range(a, b+1) if sum(int(d) ** (j+1) for j, d in enumerate(str(i))) == i]

#test
print(sum_dig_pow(1, 10))
print(sum_dig_pow(1, 100))
print(sum_dig_pow(10, 100))
print(sum_dig_pow(90, 100))