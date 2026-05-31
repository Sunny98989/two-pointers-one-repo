class Sol:
    def left_triangle(self,n: int):
        for i in range(1,n+1):
            print("* "*i)

n = int(input("Enter the size of the triangle: "))
sol = Sol()
sol.left_triangle(n)