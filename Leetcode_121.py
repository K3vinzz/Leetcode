def maxProfit(prices: list[int]) -> int:
    res = 0
    lowest = prices[0]
    for p in prices:
        if p < lowest:
            lowest = p
        elif p > lowest:
            res = max(res, p - lowest)
    return res

print(maxProfit([7,6,4,3,1]))