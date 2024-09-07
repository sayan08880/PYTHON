s1 = input("ENTER THE STRING : ")
s2 =" "
for i in range (len(s1)) :
    if s1[i] not in "ieouaAOIUE":
     s2 = s2 + s1[i]
print("ORIGINAL STRING ",s1)
print("NEW STRING ",s2)