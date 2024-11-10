# ---------- dictionary
cars = { 
    "AA3344": "Audi TT", 
    "BK4545VB": "Nissan Micro", 
    "RD4522FF": "Ferrari F12" 
}

print(cars["BK4545VB"])

del cars["AA3344"]

if "AA3344" not in cars:
    print("Good! - Del works correctlly!")

cars.update({ 
    "BK4545VB": "Nissan GT-R", 
    "JJ3329KL": "Lincoln GP-6" 
    })

print(cars)

print(cars.pop)
print(cars.fromkeys(["BK4545VB", "JJ3329KL"]))