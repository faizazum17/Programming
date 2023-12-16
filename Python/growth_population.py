#we will calculate growth of population by 2 percent each year and additonal 50 people per year, calculate how many years it will take to reach a population of 1200
import math

def nb_year(p0, percent, aug, p):
    #conver percent to decimal
    percent = percent / 100
    counter_years = 0
    while p0 < p:
        p0 = p0 * (1+percent) + aug
        counter_years += 1
        math.ceil(counter_years)
    return counter_years


#test cases
print(nb_year(1500, 5, 100, 5000)) #15
print(nb_year(1500000, 2.5, 10000, 2000000)) #10
print(nb_year(1500000, 0.25, 1000, 2000000)) #94
print(nb_year(1500000, 0.25, -1000, 2000000)) #151
print(nb_year(1500000, 0.25, 1, 2000000)) #116