# We need an empty dictionary, to store and display the letter frequencies.
word_count = {}
special_characters = "'.!@#$%^&*()-+?_=,<>/"
# Text string
text = "Later in the course, you'll see how to use the collections Counter class."
 
for letter in text:
    
    if (not letter.isspace()) and (letter not in special_characters):
        word_count[letter.lower()]=word_count.setdefault(letter.lower(),0)+1          
# Printing the dictionary
for letter, count in sorted(word_count.items()):
    print(letter, count)