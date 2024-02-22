d={1:"Biswajit",2:"Swaraj",3:"janghyasen"}
# print(d.keys())
# print(d.values())
# d.update({4:"king"})
# print(d)

# for x in d.keys():
#     print(x)


# s=int(input("enter the keys"))
# if s in d:
#     print(d[s])
# else:
#     print("not found keys")


#exception handling
s=int(input("enter the keys"))
try:
    print(d[s])
except:
    print("key not found")

