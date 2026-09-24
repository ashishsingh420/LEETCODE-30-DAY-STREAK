prices = [7, 1, 5, 3, 6, 4]

minPrice = prices[0]
maxProfit = 0

for price in prices:
    if price < minPrice:
        minPrice = price

    profit = price - minPrice

    if profit > maxProfit:
        maxProfit = profit

print(maxProfit)




# Leetcode Problem 121: Best Time to Buy and Sell Stock

# class Solution:
#     def maxProfit(self, prices: list[int]) -> int:

#         minPrice = prices[0]
#         maxProfit = 0

#         for price in prices:
#             if price < minPrice:
#                 minPrice = price

#             profit = price - minPrice

#             if profit > maxProfit:
#                 maxProfit = profit

#         return maxProfit