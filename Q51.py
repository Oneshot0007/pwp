def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

ui = int(input("Enter Number: "))
if is_prime(ui):
    print("Prime")
else:
    print("Not Prime")
