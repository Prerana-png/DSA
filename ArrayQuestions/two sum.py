#Two sum python program.
def checkpair(A, size, x):
    for i in range(0 , size-1):
        for j in range (i+1, size):
            if (A[i]+A[j]==x):
                return 1
    return 0
    
if __name__=='__main__':
    A=[1,2,4 ,5,6,9]
    size=len(A)
    x=9
    
    if checkpair(A, size, x):
        print("yes")
    else:
        print("no")