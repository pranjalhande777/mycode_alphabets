def print_r():
    for i in range(5):
        for j in range(5):
            if j == 0 or (j == 4 and i < 3) or (i == 0 or i == 2) and j < 4 or (i == 3 and j == 2) or (i == 4 and j == 3):
                print("*", end="")
            else:
               print(" ", end="")
        print()

print_r()
