def is_palindrome(s: str) -> bool:
    # Step 1: Normalize the string by filtering out non-alphanumeric characters
    normalized_str = ''.join(char.lower() for char in s if char.isalnum())
    # Step 2: Check if the normalized string is equal to its reverse
    return normalized_str == normalized_str[::-1] # reversed