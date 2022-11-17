str1=str(input("ente a string"))
print(str1)
dict={}
a=str1.split(' ')
print(a)
for a in str1:
    if a in dict:
        dict[a]+=1
    else:
        dict[a]=1
print(dict)