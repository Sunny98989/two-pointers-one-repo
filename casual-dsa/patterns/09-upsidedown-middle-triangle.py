class Sol:
    def upsidedown_middle_triangle(self,n):
        for i in range(n,0,-1):
            print(" "*(n-i),end="")
            print("* " *i)

n = int(input("enter a num:"))
sol = Sol()
sol.upsidedown_middle_triangle(n)