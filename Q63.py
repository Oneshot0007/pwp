num = input("Enter a number: ")

num_to_words = {
    '0': "Zero", '1': "One", '2': "Two", '3': "Three", '4': "Four",
    '5': "Five", '6': "Six", '7': "Seven", '8': "Eight", '9': "Nine"
}

for digit in num:
    print(num_to_words[digit], end=" ")
