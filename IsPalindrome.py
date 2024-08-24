# 9. Palindromic Number
def isPalindrome(x: int) -> bool:
    if x < 0 or (x > 0 and x%10 == 0):
        return False

    rev = 0
    while x > rev:
        rev = x%10 + 10*rev
        x //= 10
    return True if x==rev or x==rev//10 else False