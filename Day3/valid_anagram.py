def isAnagram(s,t):
    if len(s)!=len(t):
        return False
    for i in s:
        if s.count(i)!=t.count(i):
            return False
    return True
s=input()
t=input()
print(isAnagram(s,t))