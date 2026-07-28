class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = 0
        for char in s :
            n += 1
        m =0 
        for char in t :
            m += 1
        if n != m :
            return False 
        arr = [0]*256 
        for i in range(n):
            arr[ord(s[i])] += 1
            arr[ord(t[i])] -= 1
        for value in arr :
            if value != 0:
                return False 
        return True 

        