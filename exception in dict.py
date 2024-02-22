d = {1:"abs",3:"bvc",4:"huj"}
s=int(input("enter the key : "))
try:
    print(d[s])
except:
    print("key not available")  
finally:
    print("code executed")     