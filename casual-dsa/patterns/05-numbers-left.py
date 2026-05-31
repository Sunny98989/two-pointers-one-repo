class Sol:
    def numbers_left(self,n): # O(n) by string concatination
        res = ""
        for i in range(1,n+1):
            res += str(i)
            print(res)

    def numbers_left_2(self,n): # O(n) by Maths 
        curr = 0
        for i in range(1,n+1):
            curr = curr*10 + i
            print(curr)
    
    def numbers_left_3(self,n): # O(n^2) way
        for i in range(1,n+1):
            for j in range(1,i+1):
                print(j,end='')
            print()

n = int(input("Enter the size for pattern: "))
sol = Sol()
sol.numbers_left(n)
print("=================")
sol.numbers_left_2(n)
print("=================")
sol.numbers_left_3(n)