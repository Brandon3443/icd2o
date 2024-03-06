month = int(input())
day = int(input())

if month < 2:
    print("before")
elif month > 2:
    print("after")

if day < 18:
    print("before")
elif day > 18:
    print("after")
else:
    print("special")