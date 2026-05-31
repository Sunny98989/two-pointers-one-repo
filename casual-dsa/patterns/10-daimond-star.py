class Sol:
    def daimond_star(self,n):
        for i in range(1,n+1):
            print(" "*(n-i),end='')
            print("* " * i)
        for i in range(n,0,-1):
            print(" "*(n-i),end='')
            print("* " * i)
    
    def perfected_daimond_star(self,n):
        for i in range(1,n+1):
            print(" "*(n-i),end='')
            print("* " * i)
        for i in range(n-1,0,-1):
            print(" "*(n-i),end='')
            print("* " * i)

n = int(input("IM INPUT: "))
sol = Sol()
sol.daimond_star(n)
print("this is the line")
sol.perfected_daimond_star(n)