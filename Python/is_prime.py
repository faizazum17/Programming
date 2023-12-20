#is a number prime
def is_prime(num):
    if num <= 1:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
    return True

#refactored
def is_prime(num):
    return num > 1 and all(num % i for i in range(2, num))

#optimized
def is_prime(num):
    return num > 1 and all((num % i for i in range (2, int(num**0.5)+1)))

    
#test
print(is_prime(0))
print(is_prime(1))
print(is_prime(2))
print(is_prime(3))
print(is_prime(4))
print(is_prime(5))
print(is_prime(6))
print(is_prime(7))