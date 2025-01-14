# Given st & end of subarray, just print the elements of the subarray[st to end] T.C = O(N)
# IDEA: Naive approach is to run a loop from st to end and print the elements of the subarray
def solve(A, st, end):
    for i in range(st, end+1):
        print(A[i], end = " ")
    print()
    return  0





A = [6,3,3,6,7,8,7,3,7]
st = 2
end = 5
print(solve(A, st, end)) # 3 6 7 8