def print_k():
    for i in range(5):
        for j in range(5):
            if j == 0 or (i + j == 3) or (i - j == 1):
                print("*", end="")
            else:
                print(" ", end="")
        print()

print_k()
