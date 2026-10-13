class Sol:
    def alphabet_continuous(self,n):
        for i in range(1,n+1):
            for j in range(1,i+1):
                print(chr(64+i),end='')
            print()

n = int(input("IM INPUT: "))
sol = Sol()
sol.alphabet_continuous(n)