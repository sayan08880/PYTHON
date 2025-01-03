def frecuancy(string,char):
    frecuancy = string.count(char)
    print(f"{char} FREQUENCY IS {frecuancy}")

#Main

string = input("ENTER THE STRING : ")
char = input("ENTER THE CHARECTER FIND FREQUENCY : ")
frecuancy(string,char)