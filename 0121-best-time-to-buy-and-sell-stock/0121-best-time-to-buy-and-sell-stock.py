class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = float('inf')
        maxpro = 0
        for x in prices :
            if x < minprice :
                minprice = x
            profit = x - minprice 
            if profit > maxpro :
                maxpro = profit 
        return maxpro
