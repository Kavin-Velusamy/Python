# M = 9
# def puzzle(a):
#     for i in range(M):
#         for j in range(M):
#             print(a[i][j],end = " ")
#         print()
# def solve(grid, row, col, num):
#     for x in range(9):
#         if grid[row][x] == num:
#             return False
             
#     for x in range(9):
#         if grid[x][col] == num:
#             return False
 
 
#     startRow = row - row % 3
#     startCol = col - col % 3
#     for i in range(3):
#         for j in range(3):
#             if grid[i + startRow][j + startCol] == num:
#                 return False
#     return True
 
# def Suduko(grid, row, col):
 
#     if (row == M - 1 and col == M):
#         return True
#     if col == M:
#         row += 1
#         col = 0
#     if grid[row][col] > 0:
    #     return Suduko(grid, row, col + 1)
    # for num in range(1, M + 1, 1): 
     
    #     if solve(grid, row, col, num):
         
#             grid[row][col] = num
#             if Suduko(grid, row, col + 1):
#                 return True
#         grid[row][col] = 0
#     return False
 
# '''0 means the cells where no value is assigned'''
# grid = [[2, 5, 0, 0, 3, 0, 9, 0, 1],
#         [0, 1, 0, 0, 0, 4, 0, 0, 0],
#     [4, 0, 7, 0, 0, 0, 2, 0, 8],
#     [0, 0, 5, 2, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 9, 8, 1, 0, 0],
#     [0, 4, 0, 0, 0, 3, 0, 0, 0],
#     [0, 0, 0, 3, 6, 0, 0, 7, 2],
#     [0, 7, 0, 0, 0, 0, 0, 0, 3],
#     [9, 0, 3, 0, 0, 0, 6, 0, 4]]
 
# if (Suduko(grid, 0, 0)):
#     puzzle(grid)
# else:
#     print("Solution does not exist:(")




##############################################

###first 10 natural number
# for i in range(1,11):
#     print(i,end=" ")

###first 10 even numbers
# for i in range(0,21,2):
#     print(i)

###first 10 odd number
# for i in range(0,22,1):
#     print(i)

###first 10 even number in reverse order
# for i in range(22,0,-2):
#     print(i)

# ### print table of a number accepted from user.

# num=int(input("Enter the table :"))
# for i in range(1,11):
#     print(num*i,end=',')

### Write a program to display product of the digits of a number accepted from the user.

# num=int(input("Enter the number :"))
# p=1
# while(num):
#     r=num%10                                              ##dout
#     p=p*r
#     num=num//10
#     print("print the product of digit is:",p)

### Write a program to find the factorial of a number.

# num=int(input("Enter te number :"))
# f=1
# for i in range(1,num+1):
#     f=f*i
#     print("Factorial is :",f)


###Write a program to find the sum of the digits of a number accepted from user

# num=int(input("Enter the number :"))
# s=1
# while(num):
#     r=num%10                                              ##dout
#     s=s+r
#     num=num//10
#     print("print the product of digit is:",s)


###Write a program to check whether a number is prime or not.
 
num=int(input("Enter the number :"))










##############################################

