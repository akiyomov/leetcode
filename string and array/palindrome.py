def is_palindrome(word: str) -> bool:
    """Return True if word is a palindrome, False otherwise."""
    i,j = 0, len(word)-1
    while i < j:
        if word[i] != word[j]:
            return False
        i += 1
        j -= 1
    return True

print(is_palindrome('noon'))
    
