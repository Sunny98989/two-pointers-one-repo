class Sol:
    def pattern(self, n):
        for i in range(n):
            print(" " * (n-i-1), end='')
            print("*" * (i*2+1), end='')
            print(" " * (n-1-i))

n=int(input("enter the num: "))
sol = Sol()
sol.pattern(n)