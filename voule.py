def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for letter in string:
        if letter in vowels:
            count += 1
    return count

string = input("Enter a sentence: ")
vowel_count = count_vowels(string)
print("Number of vowels:", vowel_count)

