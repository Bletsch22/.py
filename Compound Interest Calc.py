principle = 0 or ""
rate = 0
time = 0



while True:
    principle = float(input("Enter Principle amount: "))
    if principle < 0:
        print("Principle cannot be equal or less than zero")
    else: 
        break
    

while True:
    rate = float(input("Enter interest rate: "))
    if rate < 0:
        print("Rate cannot be equal or less than zero")
    else:
        break

while True:
    time = int(input("Enter time in years: "))
    if time < 0:
        print("Time cannot be equal or less than zero")
    else:
        break

total = principle * pow((1+ rate / 100), time)
print(f"Balance afer {time} year/s: ${total: .2f}")