def count_good_substrings(s):
    count = 0
    for i in range(len(s) - 2):
        sub_string = s[i:i + 3]
        if len(set(sub_string)) == 3:
            count += 1
    return count

# Example usages
print(count_good_substrings("xyzzaz"))  # Output: 1
print(count_good_substrings("aababcabc"))  # Output: 4
