def count (text) :
    upper = 0
    lower = 0
    alpha = 0
    digit = 0

    for char in text :
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1

        if char.isalpha():
            alpha += 1
        elif char.isdigit():
            digit += 1
    
    return upper , lower , alpha , digit

#MAIN

string = input("ENTER THE STRING : ")
upper , lower ,alpha , digit = count(string)

print(f"UPPERCASE COUNT : {upper}")
print(f"LOWERCASE COUNT : {lower}")
print(f"ALFABATE COUNT : {alpha}")
print(f"DOGIT COUNT : {digit}")