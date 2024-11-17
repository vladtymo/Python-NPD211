# ---------- closure
def getCalculator():
    a = 10

    def inner():
        nonlocal a
        print(a)
        a += 1

    return inner

def getCalculatorUsignLambda():
    a = 10

    return lambda: a + 1

calculate = getCalculator()

print(calculate())
calculate()
calculate()

# def multiply(n):
#     def inner(m): return n * m
 
#     return inner
 
 
# fn = multiply(5)
# print(fn(5))        # 25
# print(fn(6))        # 30
# print(fn(7))        # 35
