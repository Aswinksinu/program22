string1=input("enter the first str :")
string2=input("enter the second str :")
a=string1[0]
b=string2[0]
new_str1=string2[0]+string1[1:]
new_str2=string1[0]+string2[1:]
print(new_str1+' '+new_str2)