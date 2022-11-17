a=input("enter a string")
print(a)
dict={}
for i in a:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)

print("characters")
for i,k in dict.items():
    print(i,k)