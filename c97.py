sentence = input("Enter a sentence: ")
number_of_characters = 0
number_of_words = 1

for i in sentence:
    number_of_characters += 1

    if(i == " "):
        number_of_words += 1
        
print(number_of_words)
print(number_of_characters)