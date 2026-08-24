class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest = -1
        for i in range (len (arr)-1 , -1 , -1):
            curr = arr[i]
            arr[i] = greatest 
            if curr > greatest :
                greatest = curr 
                
        return arr
            
