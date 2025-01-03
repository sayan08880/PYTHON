def find_longest_word(string):
    words = string.split()
    max_word = ""
    max_length = 0
    for word in words:
        if len(word) > max_length:
            max_word = word
            max_length = len(word)
    return max_word

string = input("Enter a sentence: ")
longest_word = find_longest_word(string)
print("The longest word is:", longest_word)
