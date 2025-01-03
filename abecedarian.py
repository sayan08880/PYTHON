def abercedarian(word) :
    return word == "".join(sorted(word))

#Main
input = input("ENTER THE STRING : ")
if abercedarian(input.lower()) :
    print(f"{input} IS ABERCEDARIAN WORD")
else:
    print(f"{input} IS'T ABERCEDARIAN WORD")