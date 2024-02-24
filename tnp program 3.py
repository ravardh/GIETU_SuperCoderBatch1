d={1:"omm",2:"anurag",3:"zxcv"}
t= int(input("Enter any key:"))
#Exception handling
try:
    print(d[t])
except:
    print("Key not available")
finally:
    print("Code Executed3")