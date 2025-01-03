num = int(input("ENTER THE NUMBER : "))
sum = 0
save = num
while num>0 :
    sum_i = num % 10
    sum = sum*10 + sum_i
    num = num // 10
if sum == save :
    print(save,"IS PALINSROM")
else :
    print(save,"IS NOT PALINDROM") 
