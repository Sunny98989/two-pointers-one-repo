class Sol:
    def true_reverse_alphabet(self,n):
        for i in range(1,n+1):
            for j in range(i,0,-1):
                print(chr(64+j),end='')
            print()

n = int(input("IM INPUT: "))
sol = Sol()
sol.true_reverse_alphabet(n)
