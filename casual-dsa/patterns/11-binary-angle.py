class Sol:
    def true_binary_angle(self,n): # totally different pattern just for fun
        count= 0
        for i in range(1,n+1):
            for j in range(1,i+1):
                if count%2 == 0:
                    print(1,end='')
                    count+=1
                else:
                    print(0,end='')
                    count+=1
            print()
    

    def binary_angle(self,n):     # brute force approach
        for i in range(1,n+1):
            for j in range(1,i+1):
                if i%2 == 0:
                    if j%2 ==0:
                        print(1,end='')
                    else:
                        print(0,end='')
                else:
                    if j%2 ==0:
                        print(0,end='')
                    else:
                        print(1,end='')
            print()
        
n = int(input("IM INPUT: "))
sol = Sol()
sol.true_binary_angle(n)
print("this is the line")
sol.binary_angle(n)