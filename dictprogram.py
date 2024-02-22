d = {1: 'Sivam',2: 'Ram',3: 'Syam',4: 'Hari'}
print(d)

for x in d:
 print(x)
for values in d.values():
 print(values)
 
s=int(input("Enter a key"))

if s in d.keys():
    print(d[s])
else:
    print("No key found")

