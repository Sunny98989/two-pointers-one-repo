class Sol:
    def right_triangle(self, n):
        for i in range(1, n + 1):
            print('  ' * (n - i), end='')
            print('* ' * i)

n = int(input("enter a num: "))
Sol().right_triangle(n)
