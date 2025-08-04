
def isPalindrome(s):
    pali=""
    for i in s:
        if i.isalnum():
            pali+=i.lower()
    if pali==pali[::-1]:
        return True
    else: 
        return False
x=input()
print(isPalindrome(x))