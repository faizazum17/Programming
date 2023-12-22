#Given an array of meals where each element is a string in the form '300g turkey, 300g potatoes, 100g cucumber' find out how many proteins and calories you consumed. 

def sum_proteins_calories(meals):
    #your code here
    #create a list of tuples
    meals = [x.split(', ') for x in meals]
    #create a list of tuples
    meals = [(int(x[0][:-1]), int(x[1][:-1])) for x in meals]
    #create a list of tuples
    meals = [(x[0], x[0]*4 + x[1]*9) for x in meals]
    #create a list of integers
    meals = [x[0] for x in meals]
    #create a list of integers
    meals = [x[1] for x in meals]
    return sum(meals)

#refactored
def sum_proteins_calories(meals):
    return sum(int(x.split(', ')[0][:-1]) * 4 + int(x.split(', ')[1][:-1]) * 9 for x in meals)