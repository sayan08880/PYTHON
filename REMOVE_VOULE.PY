def remove_vowels(string):
    vowels = "aeiouAEIOU"
    result = ""
    for letter in string:
        if letter not in vowels:
            result += letter
    return result

string = input("Enter a sentence: ")
no_vowels_string = remove_vowels(string)
print("String without vowels:", no_vowels_string)
