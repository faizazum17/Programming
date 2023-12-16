#find next perfect square
def find_next_perfect_square(sq):
    if sq < 0:
        return -1
    else:
        root = sq ** 0.5
        if (root % 1 == 0):
            return (root + 1) ** 2
        else:
            return -1

print(find_next_perfect_square(121)) #144
print(find_next_perfect_square(625)) #676
print(find_next_perfect_square(114)) #-1