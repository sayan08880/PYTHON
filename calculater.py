opp = input("ENTER THE OPPARETION( + | - | / | * | ^ ): ")
n1 = int(input("ENTER THE 1ST NUMBER: "))
n2 = int(input("ENETER THE 2ND NUMBER: "))
if opp == '+' :
    result = n1 + n2
elif opp == '-':
    result = n1 - n2
elif opp == '/':
    result = n1 / n2
elif opp == '*':
    result = n1 * n2
elif opp == '^':
    result = n1 ** n2
else:
    print(n1,opp,n2,"INPUT ERROR" )
print(n1, opp ,n2,'=',result)