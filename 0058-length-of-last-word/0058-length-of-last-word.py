class Solution(object):
    def lengthOfLastWord(self, s):
        a=list(s.split())
        l=len(a[-1])
        c=0
        while (l != 0):
            c+=1
            l-=1
        return c
  
        