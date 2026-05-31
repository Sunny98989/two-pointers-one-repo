class Sol:
    def triangle(self, n):
        for i in range(1,n+1):
            print(" "*(n-i),end="")
            print("* "*i)


n=int(input("enter the num: "))
sol = Sol()
sol.triangle(n)