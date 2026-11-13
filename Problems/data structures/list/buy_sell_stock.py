def find_maxProfit(nums):
    # max_profit=0
    # for i in range(0,len(nums)-1):
    #     for j in range(i+1,len(nums)):
    #         current_profit=nums[j]-nums[i]
    #         if max_profit < current_profit:
    #             max_profit=current_profit
    # return max_profit

    max_profit=0
    min_price=prices[0]
    print("Value od min_profite at first",min_price)
    for i in range(0,len(prices)):
        if prices[i] < min_price:
            print(f"bhai new min price mil gya interation number{i} par value hai 'prices[i]' -> {prices[i]}")
            min_price=prices[i]
        current_profit=prices[i] - min_price
        print(f"Curreant profit iteration number {i} pe {current_profit} itna hai")
        if current_profit > max_profit:
            print(f"bhai new max profit hai {current_profit}")
            max_profit=current_profit
    print(f"Done got max profit of {max_profit}")        
    return max_profit
prices=[7,1,5,3,6,4]
print("function execution start")
print(find_maxProfit(prices))