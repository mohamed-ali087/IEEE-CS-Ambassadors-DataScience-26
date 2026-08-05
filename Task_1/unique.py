word = input("Enter a word: ")

repeat = False

for letter in word:
    if word.count(letter) > 1:
        repeat = True

if repeat:
    print("Has Repeats")
else:
    print("All Unique")