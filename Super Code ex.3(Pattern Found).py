#string =ABABCABACBCABCABABCABACB pattern 'ABC'found in this string. 
#pattern=ABC
#string ="ABABCABACBCABCABABCABACB"
string=input("Enter the string:\n")
pattern=input("Enter the pattern:\n")
#pattern="ABC"
flag=False
len_pattern=len(pattern)
for i in range(len(string)):
    if(string[i:i+len_pattern]==pattern):
        print("found at:",i,"index")
        flag=True
if(flag==False):
    print("Pattern not found")
