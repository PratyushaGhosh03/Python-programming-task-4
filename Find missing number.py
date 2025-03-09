def find_missing_number(arr, n):
    expected_sum = (n * (n + 1)) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

# Example usage:
arr = [1, 2, 4, 5, 6]  # Missing number is 3
n = 6
print(find_missing_number(arr, n))  # Output: 3
