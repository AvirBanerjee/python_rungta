def find_maxProfit(nums):
    max_profit=0
    for i in range(0,len(nums)-1):
        for j in range(i+1,len(nums)):
            current_profit=nums[j]-nums[i]
            if max_profit < current_profit:
                max_profit=current_profit
    return max_profit

prices=[7,6,4,3,1]
print(find_maxProfit(prices))