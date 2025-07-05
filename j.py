def print_j():
    for i in range(5):
        for j in range(5):
            if i == 0 or (j == 2) or (i == 4 and j < 2) or (j == 0 and i == 3):
                print("*", end="")
            else:
                print(" ", end="")
        print()

print_j()
