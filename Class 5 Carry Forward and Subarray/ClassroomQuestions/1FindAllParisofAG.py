# BRUTE FORCE:-  check for all the valid pairs, if S[i] == 'g' increment the count T.C = O(N^2)
# IDEA - 1
def solve(A):
    count = 0
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[i] == 'a' and A[j] == 'g':
                count += 1
                print(count)
    return count

# Look for s[i] == 'a' and if found then only look for s[j] == 'g' and increment the count T.C = O(N^2)
# IDEA - 2
def solve(A):
    count = 0
    for i in range(len(A)):
        if A[i] == 'a':
            for j in range(i+1, len(A)):
                if A[j] == 'g':
                    count += 1
                    print(count)
    return count


# Look for s[i] == 'a' and if found then only look for s[j] == 'g' and increment the count T.C = O(N)
# IDEA - 3
def solve(A):
    count = 0
    a_count = 0
    for i in range(len(A)):
        if A[i] == 'a':
            a_count += 1
        if A[i] == 'g':
            count += a_count
        print(count)
    return count










A = "agagag"
solve(A) # 3