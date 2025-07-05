def print_e():
    for i in range(5):
        for j in range(5):
            if j == 0 or (i == 0 or i == 2 or i == 4):
                print("*", end="")
            else:
                print(" ", end="")
        print()

print_e()


