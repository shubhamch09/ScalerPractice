# Brute Force Approach : go and get the subarray, for each subarray we will itrerate on it, 
# Add all the elements of the subarray and then finally add it to the total sum T.C = O(N^3)

# def solve(A):
#     N = len(A)
#     TotalSum = 0    

#     for i in range(N):
#         for j in range(i, N):
#             Sum = 0
#             for k in range(i, j+1):
#                 Sum += A[k]
#             TotalSum += Sum


#     return TotalSum





# Approach 2 : Using prefix sum T.C = O(N^2)

# def solve(A):
#     N = len(A)

#     prefixsumarray = [0] * (N)
#     prefixsumarray[0] = A[0]
#     totalsum = 0
#     for i in range(1,N):
#         prefixsumarray[i] = A[i] + prefixsumarray[i-1]


#     for i in range(N):
#         for j in range(i, N):
#             if i == 0:
#                 totalsum += prefixsumarray[j]
#             else:
#                 totalsum += prefixsumarray[j] -prefixsumarray[i-1]

#     return totalsum




# Approach 3 : using carry forward technique
# before that understand this question 

#  given A[] of len N print sum stating from index 3




# def solve(A,B):
#     sum = 0
#     N = len(A)
#     for i in range(B,N):
#         sum += A[i]

#     print(sum)


# B = [2,8,4,7,-9,4,3,-2]
# C = 3

# print(solve(B,C))


# Approach 3 : Carry Forward

def solve(A):
    totalsum = 0
    N = len(A)

    for i in range(N):
        sum = 0
        for j in range(i,N):
            sum += A[j]
            totalsum += sum

    print(totalsum)




# Most Optimal Approach Using the Contribution technique With T.C = O(N)

#  Contribution of each element  = for index i  = (i+1) *(N- i)
# sum = element * contribution 


# def solve(A):

#     N = len(A)
#     totalsum = 0
#     for i in range(N):
#         contribution = (i+1)* (N-i)
#         totalsum += A[i] * contribution

#     print(totalsum) 


A = [1, 2, 3]   
print(solve(A)) # 20




