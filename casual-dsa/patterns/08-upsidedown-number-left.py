import sys


class Sol:
    def upsidedown_numbers_pattern(self,n): #O(n^2) no questions about it, we are using nested loops
        for i in range(n,0,-1):
            for j in range(1,i+1):
                print(j,end='')
            print()


    def upsidedown_2(self,n): # yup still O(n^2) even thoqh we are not using nested loops, 
        res = ""              # we are slicing the string which is O(n) and we are doing it n times so O(n^2)
        for i in range(1,n+1):
            res += str(i)
        for j in range(n,0,-1):
            print(res[:j])
        
    def upsidedown_3(self,n): # O(n^2) still because its python if used another language it would be O(n).
        curr = 0              # IN THEORY 
        for i in range(1,n+1):
            curr = curr*10 + i
        for j in range(n,0,-1):
            print(curr)
            curr //= 10


    def upsidedown_optimized(self, n): # from gemini
        # 1. Pre-allocate the entire sequence as a single string.
        # This is exactly O(n) operations and memory.
        full_str = "".join(str(i) for i in range(1, n + 1))
        
        # 2. Bypass standard 'print' and write directly to the I/O stream.
        # 'print()' adds invisible overhead (checking arguments, formatting).
        # sys.stdout.write is Python's fastest way to push text to the console.
        out = sys.stdout.write
        
        # 3. Slice and write. Slicing in Python is highly optimized in C under the hood.
        # This loop is technically O(n^2) total work due to slicing and I/O, 
        # but it is blindingly fast compared to mathematical operations.
        for j in range(n, 0, -1):
            out(full_str[:j] + '\n')

n = int(input("enter a num:"))
sol = Sol()
sol.upsidedown_numbers_pattern(n)
sol.upsidedown_2(n)
sol.upsidedown_3(n)
sol.upsidedown_optimized(n)