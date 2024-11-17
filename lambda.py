import math

# -------------- lambda as parameter
def changeList(list, modifier):
    for i in range(len(list)):
        list[i] = modifier(list[i])

numbers = [45, 2, -1, 0, 99, 120, 34, 12]
# changeList(numbers, lambda n: n * n)
changeList(numbers, lambda n: n + 2)
changeList(numbers, lambda n: n * -1)
# changeList(numbers, lambda n: math.pow(n, 3))

print(numbers)

# -------------- lambda as return value
def select_operation(choice):
    if choice == 1:
        return lambda a, b: a + b
    elif choice == 2:
        return lambda a, b: a - b
    else:
        return lambda a, b: a * b
 
 
operation = select_operation(1)  # operation = sum
print(operation(10, 6))  # 16
 
operation = select_operation(2)  # operation = subtract
print(operation(10, 6))  # 4
 
operation = select_operation(3)  # operation = multiply
print(operation(10, 6))  # 60