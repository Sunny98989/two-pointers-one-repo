class Sol:
    def left_triangle(self, n):
        for i in range(1,(2*n)+1):
            if i <= n:
                print("*" * i)
            else:
                print("*" * ((2*n)-i))


n = int(input("YO DROP A NUMBER: "))
sol = Sol()
sol.left_triangle(n)