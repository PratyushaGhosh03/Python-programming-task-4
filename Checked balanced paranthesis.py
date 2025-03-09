def is_balanced(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or stack.pop() != mapping[char]:
                return False
    return not stack

# Example usage:
print(is_balanced("(){}[]"))  # Output: True
print(is_balanced("{[()]}"))  # Output: True
print(is_balanced("{[(])}"))  # Output: False
