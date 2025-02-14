#shipping weight comparison
weight = 4.8
premium = 125

#Ground shipping
if weight <= 2:
    price = weight * 1.50 + 20.00
elif weight <= 6:
    price = weight * 3.00 + 20.00
elif weight <= 10:
    price = weight * 4.00 + 20.00
else:
    price = weight * 4.75 + 20.00

print("Ground Shipping:", price)

#Ground Shipping Premium
print("Premium:",premium)

#drone shipping
if weight <= 2:
    price = weight * 4.50 
elif weight <= 6:
    price = weight * 9.00 
elif weight <= 10:
    price = weight * 12.00 
else:
    price = weight * 14.25
print("Drone Shipping:", price)
