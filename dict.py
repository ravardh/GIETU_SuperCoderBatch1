d1={1:2,3:4,6:323}
print("Enter the key you want the value for :")
a=int(input())
try:
    print(f"The value of key {a} is the value {d1[a]}")
except KeyError:
    print("KeyError aarha hai yaar !! Kya kar rha hai ? Sahi se daalo key !")