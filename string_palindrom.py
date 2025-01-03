def palindrome(char):
    if char == char[::-1]:
        print(f"{char} ---> IS PALINDROM")
    else:
        print(f"{char} ---> IS NOT PALINDROME")

#MAIN
string = input("ENTER THE STRING : ")
palindrome(string)

