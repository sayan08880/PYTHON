
input_str = input("ENTER THE STRING: ")

upper = 0
lower = 0
digit = 0


for c in input_str:
    if c.isupper():
        upper += 1
    elif c.islower():  
        lower += 1
    elif c.isdigit():  
        digit += 1


print("UPPERCASE LETTERS : ", upper)
print("LOWERCASE LETTERS : ", lower)
print("DIGITS : ", digit)
