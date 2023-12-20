#function to find prime factor decomposition of a number. the result will be a string with the following form:
# "(p1**n1)(p2**n2)...(pk**nk)"
def prime_factors(n):
    #your code here
    if n == 1:
        return "(1)"
    else:
        result = ""
        for i in range(2, n+1):
            count = 0
            while n % i == 0:
                count += 1
                n /= i
            if count > 0:
                if count == 1:
                    result += "(" + str(i) + ")"
                else:
                    result += "(" + str(i) + "**" + str(count) + ")"
            if n == 1:
                return result
        return result

    
#test
print(prime_factors(7775460))
print(prime_factors(7919))
print(prime_factors(1))
    