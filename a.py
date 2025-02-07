def print_a():
    for i in range(5):
        for j in range(5):
            if (j == 0 or j == 4) and i != 0 or (i == 0 or i == 2) and (0 < j < 4):
                print("*", end="")
            else:
                print(" ", end="")
        print()

print_a()
