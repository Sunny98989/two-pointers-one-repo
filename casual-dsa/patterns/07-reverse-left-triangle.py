def reverse_triangle(n):
    for i in range(n, 0, -1):
        print("* " * i)

n = int(input("Enter the size of the triangle: "))
reverse_triangle(n)