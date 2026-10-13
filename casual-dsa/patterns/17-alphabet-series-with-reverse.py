class Sol:
    def alphabet_continuous(self,n):
        res = ''
        for i in range(1,n+1):
            print(" " * (n-i),end='')
            res += chr(64+i) 
            if i == 1:
                print(res)
            else:
                print(res,end='')
                print(res[:-1][::-1])
            

n = int(input("IM INPUT: "))
sol = Sol()
sol.alphabet_continuous(n)