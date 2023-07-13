print(" *** Wind classification ***")
km = float(input("Enter wind speed (km/h) : "))
if km > 0.00 and km <= 51.99:
    print("Wind classification is Breeze.")
elif km >= 52.00 and km < 55.99:
    print("Wind classification is Depression.")
elif km >= 56.00 and km < 101.99:
    print("Wind classification is Tropical Storm.")
elif km >= 102.00 and km < 208.99:
    print("Wind classification is Tropical.")
elif km >= 209.00:
    print("Wind classification is Super Typhoon.")