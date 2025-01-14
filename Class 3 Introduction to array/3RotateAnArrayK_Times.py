def solve(A,B):
    if  B > len(A):
        B = B % len(A)
    
    def reverse(C,D,E):
        while D<E:
            C[D], C[E] = C[E], C[D]
            D += 1
            E -= 1
        
        return C
    
    F = 0
    G = len(A) - 1

    X = reverse(A , F ,G)
    Y = reverse (X , 0 , B-1)
    Z = reverse(Y, B , G)

    return Z

solve([1,2,3,4,5], 2)
