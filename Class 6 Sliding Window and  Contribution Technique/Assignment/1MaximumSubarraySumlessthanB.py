# Advance
    # @param A : list of integers
    # @param B : integer
    # @return an integer


# brute force approach
# def solve(A, B):
#     count = 0
#     N = len(A)
#     for i in range(N):
#         sum = 0
#         for j in range(i,N):           
#             sum = 0
#             for k in range (i,j+1):
#                 sum += A[k]
#             if ((j - i + 1) % 2 == 0 ) and sum < B:
#                 count += 1
#             if ((j - i + 1) % 2 != 0 ) and sum > B:
#                 count += 1
#     return count


# sliding window technique T.C = O(N^2)

def solve(A,B):
    N = len(A)
    count = 0

    for i in range(N):
        currentsum = 0
        for j in range(i,N):
            currentsum += A[j]

            currentRange = j-i+1

            if (currentsum > B and currentRange % 2 != 0) or (currentsum < B and currentRange % 2 == 0) :
                count += 1

A = [13, 16, 16, 15, 9, 16, 2, 7, 6, 17, 3, 9]
B = 65
solve(A,B)




