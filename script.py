#!/usr/bin/env python3
import re

# Change the functions below to determine if the given input is a palindrome.

def is_palindrome(s):
    
    cleaned = re.sub(r"[^\d\w]", "", s.lower())
    if cleaned == "":
        return True
    if len(cleaned) == 1:
        return True
    if len(cleaned) == 2:
        return cleaned[0] == cleaned[-1]

    if cleaned[0] == cleaned[-1]:
        return True and is_palindrome(cleaned[1:-1])
    else: return False




# The following lines call the function and prints the return
# value to the Console. This way you can check what it does.
print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("No lemon, no melon"))
print(is_palindrome("This is not a palindrome"))
print(is_palindrome("***"))
