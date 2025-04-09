rows = 4
for i in range(rows):
    # Print spaces to center the pyramid
    print(" " * i, end="")

    # Calculate how many characters to print: 2*(rows - i) - 1
    for j in range(2 * (rows - i) - 1):
        print("1" if j % 2 == 0 else "0", end="")
    print()
