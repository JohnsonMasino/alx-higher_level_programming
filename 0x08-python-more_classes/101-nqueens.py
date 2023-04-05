#!/usr/bin/python3
"""
This is nqueens backtracking program which prints the coordinates of n queens
on an nxn grid so that they all are in a non-attacking positions
"""


from sys import argv

if __name__ == "__main__":
    a = []
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    var1 = int(argv[1])
    if var1 < 4:
        print("N must be at least 4")
        exit(1)

    #to initialize the answer list,
    for i in range(var1):
        a.append([i, None])

    def already_exists(y):
        """check that a queen does not already exist in that y value"""
        for x in range(var1):
            if y == a[x][1]:
                return True
        return False

    def reject(x, y):
        """determines whether or not to reject the solution"""
        if (already_exists(y)):
            return False
        i = 0
        while(i < x):
            if abs(a[i][1] - y) == abs(i - x):
                return False
            i += 1
        return True

    def clear_a(x):
        """clears the answers from the point of failure on"""
        for i in range(x, var1):
            a[i][1] = None

    def nqueens(x):
        """recursive backtracking function to find the solution"""
        for y in range(var1):
            clear_a(x)
            if reject(x, y):
                a[x][1] = y
                if (x == var1 - 1):  # accepts the solution
                    print(a)
                else:
                    nqueens(x + 1)  # moves on to next x value to continue

    # must start the recursive process at x = 0
    nqueens(0)
