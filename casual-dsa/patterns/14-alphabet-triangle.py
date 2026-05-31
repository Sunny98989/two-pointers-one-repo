class Sol:
    def letter_triangle(self, n):
        for i in range(1, n + 1):
            for j in range(i):
                print(chr(65 + j), end="")
            print()

n = int(input("Enter the number: "))
sol = Sol()
sol.letter_triangle(n)