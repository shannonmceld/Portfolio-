# TODO
import re

# Ask for user input
text = input("Text: ")

# get each letter in input
letter = re.findall("[a-zA-Z]", text)

# get each sentence in input
sentence = re.findall("[.!?]", text)

# count each sentence in input
sentence_count = len(sentence)

# count each letter in input
letter_count = len(letter)

# get each word and loop through to count each word
words = text.split()
count_word = 0
for word in words:
    count_word += 1

# Calculate index
s = ((sentence_count / count_word) * 100.00) * .296
l = ((letter_count / count_word) * 100) * 0.0588

index = (l - s) - 15.8

# round index
grade = round(index)

# print each grade index
if grade <= 1:
    print("Before Grade 1")

elif grade >= 16:
    print("Grade 16+")

else:
    print(f"Grade {grade}")
