def solve( A, B, C):

    while B < C:
       TEMP = A[B] 
       A[B] = A[C]
       A[C] = TEMP
       B+=1
       C -= 1
    print(A)
    return A


solve([1,2,3,4,5,6,7,8,9], 3,7)