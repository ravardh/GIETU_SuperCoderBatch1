i={1:"ruchi",2:"krushna",3:"sradha"}
t=int(input("Enter a key"))
try:
    print(i[t])
except KeyError:
    print("No such key found") 
finally:
    print("Code not executed")
