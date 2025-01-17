# you are given an integer A find all the number of noble integers in the array
# Noble integer is the integer  # count of elements < element == element itself


def solve(A):

    N = len(A)
    returnAnswer = 0

    for i in range(N):
        count = 0
        if A[i] >= 0:
            
            for j in range(N):

                if A[j] < A[i]:
                    count +=1

        if count == A[i]:
            returnAnswer +=1

    return returnAnswer


A =[-1,-5,3,5,-10,4]

print(solve(A))
