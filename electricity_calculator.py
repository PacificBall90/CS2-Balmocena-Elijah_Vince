# Electricity Bill Calculator
RATE = 12.90

while True:
    name = input("Enter customer name: ")
    if name.strip() == "":
        print("ERROR - Input is empty. Please type a valid name.")
    else:
        break
while True:
    previous = float(input("Enter previous meter reading: "))
    if previous < 0:
        print("ERROR - Input is an impossible value. Please type a valid reading.")
    else:
        break       
while True:
    current = float(input("Enter current meter reading: "))
    if current < previous:
        print("ERROR - Input is an impossible value. Please type a valid reading.")
    else:
        break

consumption = current - previous
total_bill = consumption * RATE

print("\nCustomer:", name)
print("Electricity Consumption:", consumption, "kWh")
print("Total Bill: PHP", round(total_bill, 2))

# Validation rules
# 1. Customer name -- Must not be empty
# 2. Previous reading -- Number at least 0
# 3. Current reading -- Number at least the previous reading
