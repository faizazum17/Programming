# function that returns True if the walk the app gives you will take you exactly ten minutes and will return you to your starting point, otherwise return False
def valid_walk(walk):
    #your code here
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')

#test
print(valid_walk(['n','s','n','s','n','s','n','s','n','s'])) # True
print(valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e'])) # False
print(valid_walk(['w'])) # False
print(valid_walk(['n','n','n','s','n','s','n','s','n','s'])) # False
print(valid_walk(['n','s','e','w','n','s','e','w','n','s'])) # True
print(valid_walk(['n','s','e','w','n','s','e','w','n','s','n','s','e','w','n','s','e','w','n','s'])) # False