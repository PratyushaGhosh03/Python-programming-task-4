def subarray_sum(arr, target):
    left, curr_sum = 0, 0
    for right in range(len(arr)):
        curr_sum += arr[right]
        while curr_sum > target and left <= right:
            curr_sum -= arr[left]
            left += 1
        if curr_sum == target:
            return (left, right)  # Return start and end indices
    return -1  # No subarray found

# Example usage:
arr = [1, 4, 20, 3, 10, 5]
target = 33
print(subarray_sum(arr, target))  # Output: (2, 4)
