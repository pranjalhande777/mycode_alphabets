def print_b():
    for i in range(5):
        for j in range(5):
            if j == 0 or (j == 4 and (i != 0 and i != 2 and i != 4)) or (i == 0 or i == 2 or i == 4) and j < 4:
                print("*", end="")
            else:
                print(" ", end="")
        print()

print_b()
