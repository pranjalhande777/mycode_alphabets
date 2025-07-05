def print_p():
    for i in range(5):
        for j in range(5):
            if j == 0 or (j == 4 and i < 3) or (i == 0 or i == 2) and j < 4:
                print("*", end="")
            else:
                print(" ", end="")
        print()

print_p()
