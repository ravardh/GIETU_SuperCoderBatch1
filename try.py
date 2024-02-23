i={1:"sradha",2:"miku",3:"satya"}
n=int(input("enter a key:"))
try:
    print(i[n])
except KeyError:
    print("no key")
finally:
    print("code executed")
    