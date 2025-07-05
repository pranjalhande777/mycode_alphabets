def print_u():
    for i in range(5):
        for j in range(5):
            if (j == 0 or j == 4) and i < 4 or i == 4 and (j > 0 and j < 4):
                print("*", end="")
            else:
                print(" ", end="")
        print()

print_u()
