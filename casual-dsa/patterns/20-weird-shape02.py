class Sol():
    def weird_shape_2(self, n):
        for i in range(n):
            print("*" * i, end='')
            print("  " * (n - i), end='')  #double space here! 2 * (5-0)
            print("*" * i)
        for i in range(n,0,-1):
            print("*" * i, end='')
            print("  " * (n - i), end='')
            print("*" * i)

sol = Sol()
n = int(input("I SAID GIMME A NUMBER DAMN IT!: "))
sol.weird_shape_2(n)