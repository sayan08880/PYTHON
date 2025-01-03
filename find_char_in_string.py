def celculate(string,char) :
    if char in string :
       index = string.index(char) 
       print(f"{char} IN FOUND STRING INDEX {index +1}")
    else :
       print(f"{char} IS NOT FOUND IN STRING")

#main

string = input("ENTER THE STRING : ")
char = input("ENTER THE SHERCH ELEMENT IN STRING : ")
celculate(string,char) 