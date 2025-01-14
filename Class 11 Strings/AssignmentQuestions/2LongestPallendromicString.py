def find_longest_palindromic_substring(A):

    N = len(A)
    def expand_around_center(left_index, right_index):
        # Expand around the center as long as it's a palindrome
        while left_index >= 0 and right_index < N and A[left_index] == A[right_index]:
            left_index -= 1
            right_index += 1
        # Return the bounds of the palindrome
        return left_index + 1, right_index - 1
    
    # To store the indices of the longest palindrome
    longest_start = 0
    longest_end = 0 
    
    for center in range(N):
        # Check for odd-length palindromes (single center)
        start_odd, end_odd = expand_around_center(center, center)
        # Check for even-length palindromes (double center)
        start_even, end_even = expand_around_center(center, center + 1)

        # Update the longest palindrome if the odd-length one is longer
        if end_odd - start_odd > longest_end - longest_start:
            longest_start, longest_end = start_odd, end_odd

        # Update the longest palindrome if the even-length one is longer
        if end_even - start_even > longest_end - longest_start:
            longest_start, longest_end = start_even, end_even

    # Return the longest palindromic substring
    return A[longest_start:longest_end + 1]

# Example Usage
test_string = "aaaabaaa"
print(find_longest_palindromic_substring(test_string))  # Output: "aaabaaa"
