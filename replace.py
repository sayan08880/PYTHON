def replace_is_with_are(string):
    return string.replace("is", "are")

string = input("Enter a sentence: ")
updated_string = replace_is_with_are(string)
print("Updated string:", updated_string)
