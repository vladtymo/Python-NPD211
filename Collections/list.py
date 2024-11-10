import math
# ------------ list ------------
myList = ["red", 123, True, -1, "hello"]

if "red" in myList:
    print("Yes")
else:
    print("No")


for i in myList:
    print(i)

print("-----------------")
numbers = [1, 5, 432, 12, -9, -3, 4, 450, 33, 4]

print(numbers[2]) # 432
print(numbers[-1]) # 33

# object.method()
# function(...)

numbers.append(77)

for i in range(0, len(numbers)):
    print(numbers[i])

# ----- make copy
sCopy = numbers         # shallow copy
dCopy = numbers.copy()  # deep copy

newList1 = numbers[:4]
newList2 = numbers[2:4]
newList3 = numbers[2:9:3] # start:end:step

print(newList1)
print(newList2)
print(newList3)

numbers.count(4) # 2

try:
    numbers.index(2)
except Exception:
    print("'2' does not found")

print(numbers.sort(key=abs))
print(numbers)

print(f"Mapped: {list(map(lambda x: x * x, numbers))}")

if [1,2,3] == [1,2,3]:
    print("Lists are equal!")

wordLetters = list("Hello")
print(wordLetters)

# ---- deleting
numbers.remove(5)
del numbers[3]