
def NWD(a,b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))

print(f"NWD liczb: ",a,"i",b, "jest:", NWD(a,b))
