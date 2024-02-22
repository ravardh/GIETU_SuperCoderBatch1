s= int(input("enter key"))
dict = { 1:"sneha", 2:"sanchita",3 :"sushree"}
try:
    print(dict[s])

except KeyError:
    print("This key doesnt exist")
    
else:
    print(dict[s])
finally:
    print("code executed")

