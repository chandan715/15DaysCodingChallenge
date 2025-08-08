class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a=""
        for i in digits:
            a=a+str(i)
        b=int(a)+1
        c=[]
        for j in str(b):
            c.append(int(j))
        return c
            