class Sol:
    def series_shape(self,n):
        count = 1
        for i in range(1,n+1):
            for j in range(1,i+1):
                print(count,end=' ')
                count+=1
            print()

    def series_shape_single_loop(self, n):
        total_numbers = (n * (n + 1)) // 2
        
        row_capacity = 1       
        current_row_count = 0
        
        for count in range(1, total_numbers + 1):
            print(count, "", end='')
            current_row_count += 1
            
            if current_row_count == row_capacity:
                print()
                row_capacity += 1
                current_row_count = 0


n = int(input("IM INPUT: "))
sol = Sol()
sol.series_shape(n)
print("B        O        R        D        E        R        L        I        N        E")
sol.series_shape_single_loop(n)