def add(n):
    def adder(x):
        return add(n + x)
    adder.__call__ = lambda: n
    return adder

#test
print(add(1)(2)())
print(add(1)(2)(3)())
