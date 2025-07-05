def print_g():
    for i in range(5):
        for j in range(5):
            if (j == 0 and i != 0 and i != 4) or (i == 0 or i == 4) and j > 0 or (i == 3 and j >= 2) or (j == 4 and i >= 2):
                print("*", end="")
            else:
                print(" ", end="")
        print()

print_g()
