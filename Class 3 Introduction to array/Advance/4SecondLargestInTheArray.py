def solve(A):
    secondLargest = -1
    largest = A[0]

    if len(A) == 1:
        return secondLargest 

    for i in A:
        if i > largest:
            largest = i

    
    for i in A:
        if i < largest and i > secondLargest:
            secondLargest = i
    print(largest, secondLargest)


    if largest - secondLargest == 0:
        return -1
    else:
        return secondLargest
    
A = [2, 2, 2] 
solve(A)