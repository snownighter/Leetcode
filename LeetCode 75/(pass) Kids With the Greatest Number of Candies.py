def kidsWithCandies(candies, extraCandies):
    max_candies = max(candies)  # 找出糖果數目中的最大值
    result = []
    for candy in candies:
        if candy + extraCandies >= max_candies:
            result.append(True)
        else:
            result.append(False)
    return result
