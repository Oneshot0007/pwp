def count_case_letters(text):
    upper_count = 0
    lower_count = 0

    for char in text:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    print("Original String:", text)
    print("Uppercase letters:", upper_count)
    print("Lowercase letters:", lower_count)

# Example usage
user_input = input("Enter a string: ")
count_case_letters(user_input)
