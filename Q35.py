def is_palindrome(str):
  for s in str:
    s.replace().lower()
    return s==s[::-1]
user_input = input("Enter a string: ")
if is_palindrome(user_input):
    print("It's a palindrome!")
else:
    print("Not a palindrome.")