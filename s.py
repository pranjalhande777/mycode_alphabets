def print_s():
    for i in range(5):
        for j in range(5):
            if (i == 0 or i == 2 or i == 4) and j < 4 or (j == 0 and i < 2) or (j == 4 and i > 2):
                print("*", end="")
            else:
                print(" ", end="")
        print()

print_s()
