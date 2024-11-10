# -------- set collection ---------
keys = {45, 120, 120, 43, 45}

print(keys)

copy = keys
keys.add(55)
print(keys.union([120, 130, 140]))
print(keys.intersection([120, 130, 140]))

# keys[0] = 46 - cannot change, only add/remove

print(keys)
print(copy)

for i in keys: 
    print(i)