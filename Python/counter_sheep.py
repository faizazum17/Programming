# function that counts the number of sheep present in the array 
def count_sheeps(arrayOfSheeps):
    # TODO May the force be with you
    #create a list of integers
    arrayOfSheeps = [1 if x == True else 0 for x in arrayOfSheeps]
    return sum(arrayOfSheeps)

