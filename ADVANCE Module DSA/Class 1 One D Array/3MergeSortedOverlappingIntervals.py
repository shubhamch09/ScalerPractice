def solve(A):
    # Initialize an empty list to store merged intervals
    returnArray = []
    
    for start, end in A:
       
        if not returnArray or returnArray[-1][1] < start:
            returnArray.append([start, end])
            print(returnArray)
        else:
           
            returnArray[-1][1] = max(returnArray[-1][1], end)
            print(returnArray)
    
    return returnArray

# Test case
A = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(solve(A))
