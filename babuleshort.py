my_list = [10,25,50,30,80]
leny = len(my_list)
for i in range (leny) :
    for j in range (0,leny-i-1) :
       if my_list [j] > my_list[j+1] :
           my_list[j],my_list[j+1]= my_list[j+1],my_list[j]
print("SHORTED LIST : ",my_list)
