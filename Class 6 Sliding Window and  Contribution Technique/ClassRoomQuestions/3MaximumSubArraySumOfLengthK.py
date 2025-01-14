# Given an Array A of size N print maximum subarray sum of length K

# Brute Force Approach : For every subarray of size K calculate the ssum and update if maximum


# def solve(A,K):
#     st = 0
#     end = K-1
#     N = len(A)
#     maximumsum = float("-inf")

#     while end < N:
#         sum = 0

#         for i in range(st, end+1):
#             sum += A[i]

#         if sum > maximumsum:
#             maximumsum = sum

#         st += 1
#         end += 1

#     print(maximumsum)




# ###################################------------------------------------------------------###########################
# Idea 2 : prefix sum approach T.C = O(N)

def solve(A,K):

    N = len(A)
    prefixsumarray = [0]*N
    prefixsumarray[0] = A[0]

    for i in range(1,N):
        prefixsumarray[i] = A[i] + prefixsumarray[i-1]

    
    st = 0
    end = K-1
    totalsum  = float("-inf")
    while end < N:
        sum = 0

        if st == 0:
            sum  = prefixsumarray[st]
        
        else:
            sum = prefixsumarray[end] - prefixsumarray[st - 1]


        if totalsum < sum:
            totalsum = sum

        st += 1
        end += 1

    print (totalsum )


# ###################################------------------------------------------------------###########################

# Idea 3 : sliding window technique (Carry forward + Fixed size window technique)

def solve(A,K):
    N = len(A)

    Totalsum = float("-inf")
    sum = 0
    # Creating the first window
    for i in range(K):
        sum += A[i]

    if (sum > Totalsum):
        Totalsum = sum
    
    st = 1
    end = K

    while (end < N):
        sum = sum - A[st -1] + A[end]
        if sum > Totalsum:
            Totalsum = sum 

        st += 1
        end += 1


    print( Totalsum)





A = [-3,4,-2,5,3,-2,8,2]
K = 5

solve(A,K)