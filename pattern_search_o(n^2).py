#string =ABABCABACBCABCABABCABACB
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
    print("Pattern not found")

#ABCABABABCA
#00012121234 LONGEST PREFIX AND SUFFIX

#AAABCA
#012001
    
#ABCABCAD
#00012340

'''
while i<M:
    if pat[i]==pat[len]:
            len+=1
            lps[i]=len
            i+=1
    else:
        if len!=0:
           len=lps[len-1]
        else:
        lps[i]=0
        i+=1

'''
        

