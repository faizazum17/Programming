#function that will add numbers together when called in succession.
# We also want to be able to continue to add numbers to our chain.

def add(n):
    def adder(x):
        return add(n + x)
    adder.__call__ = lambda: int(n)
    return adder

#test
print(add(1)(2))
print(add(1)(2)(3))


