def print_c():
    for i in range(5):
        for j in range(5):
            if j == 0 and (i != 0 and i != 4) or (i == 0 or i == 4) and j > 0:
                print("*", end="")
            else:
                print(" ", end="")
        print()

print_c()
