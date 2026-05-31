class Solution:
    def printBox(self, n: int):
        for i in range(1,n+1):
            print("* "*n)
    
n= int(input("Enter the size of the box: "))
sol = Solution()
sol.printBox(n)