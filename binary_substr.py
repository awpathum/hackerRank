# def countBinarySubstrings(s: str) -> int:
#     n = len(s)
#     result = 0

#     # 'left' marks the start of the previous group (all 0s or all 1s)
#     left = 0

#     # 'right' scans the string to find group boundaries
#     for right in range(1, n):

#         # A change means a new group starts
#         if s[right] != s[right - 1]:

#             # Length of the previous group
#             first_group_length = right - left

#             # Count length of the current group
#             temp = right
#             while temp < n and s[temp] == s[right]:
#                 temp += 1
#             second_group_length = temp - right

#             # Valid substrings come from pairing the two groups
#             result += min(first_group_length, second_group_length)

#             # Move 'left' to the start of the current group
#             left = right

#     return result

def countBinarySubstrings(s: str) -> int:
    # Length of the previous group of identical characters
    left = 0

    # Length of the current group we are scanning
    right = 1

    total = 0

    # Start from the second character and scan the string
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            # Same character continues the current group
            right += 1
        else:
            # Group boundary found — count valid substrings
            total += min(left, right)

            # Move the window forward
            left = right
            right = 1

    # Count substrings formed by the last two groups
    total += min(left, right)

    return total



count = countBinarySubstrings("01")
print(count)