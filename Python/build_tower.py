#function that builds a pyramid shaped tower, given the number of floors and represented with "*" characters
def tower_builder(n):
    #your code here
    return [("*" * i).center(n*2-1) for i in range(1, n*2, 2)]

#test
print(tower_builder(1))
print(tower_builder(2))
print(tower_builder(3))
print(tower_builder(4))
print(tower_builder(5))