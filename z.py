def print_z():
    for i in range(5):
        for j in range(5):
            if i == 0 or i == 4 or i + j == 4:
                print("*", end="")
            else:
                print(" ", end="")
        print()

print_z()
