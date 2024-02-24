s = input("Enter string (jismein pattern khojna hai aapko): ")
p = input("Pattern daalen : ")

# Brute Force

c=0
for i in range(len(s)-len(p)+1):
    if  s[i:i+len(p)] == p:
        c=c+1
print(c)



# Optimizing { nhin hua merese } (learned LPS) (Need to learn KMP)
