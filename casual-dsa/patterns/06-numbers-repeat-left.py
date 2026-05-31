class Sol:
    def repeated_nums(self,n):
        for i in range(1,n+1):
            print(str(i)*i)
    

    def repeated_nums_2(self,n):
        for i in range(1,n+1):
            print(i * (10**i - 1) // 9)

            
n = int(input("enter the num: "))
sol = Sol()
sol.repeated_nums(n)
sol.repeated_nums_2(n)