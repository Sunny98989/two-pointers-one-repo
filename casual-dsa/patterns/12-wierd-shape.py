class Sol:
    def weird_shape(self,n):
        sum = ""
        for i in range(1,n+1):
            sum+=str(i)
            print(sum,end='')
            print("  "*(n-i),end='')
            print(sum[::-1])

    
n = int(input("IM INPUT: "))
sol = Sol()
sol.weird_shape(n)
