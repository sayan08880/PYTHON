num = int(input("ENTER THE NUMBER : "))
num_str = str(num)
num_len = len(num_str)
save = num
total = 0

for i in num_str :
    total += int(i) ** num_len 
if (total == save):
   print(num,"IS ARMSTRONG NUMBER")
else :
   print(num,"IS NOT ARMSTRONG NUMBER") 