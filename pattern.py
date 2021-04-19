
def x(n):
    k=n-1
    for i in range(0,n):
        for j in range (0,k):
            print(end=" ")
        k-=1
        for j in range(0,i):
            print("*",end=" ")
        print("\r")

n = int(input("ENTER NUMBER ? "))

x(n)