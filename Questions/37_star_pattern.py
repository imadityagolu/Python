'''
***
* *
***
'''

n = 3
for i in range(1, n+1):
    for j in range(1, n+1):
        if(i==1 or i==n or j==1 or j==n):
            # 1st i=1 j=1 -> i == 1 or i == n/3 or j == 1 or j/1 == n/3
            # 2nd i=2 j=2 -> i == 1 or i == n/3 or j == 1 or j/2 == n/3
            # 3rd i=3 j=3 -> i == 1 or i == n/3 or j == 1 or j/3 == n/3
            print("*", end="") # end="" is used to continue printing in the same line, not move to the next line
        else:
            print(" ", end="")
    print()