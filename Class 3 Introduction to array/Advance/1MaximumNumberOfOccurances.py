def solve(A,B):
    Count = 0

    for i in A:
        if i == B:
            Count += 1
    print(Count)
    return Count
    
    
                

        
A = [1,2,3,4,5,4,3,2,2,4,6,6,6,6]
solve(A, 6)