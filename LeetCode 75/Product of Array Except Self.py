def productExceptSelf(nums):
    n = len(nums)
    output = [1] * n

    # 計算左側乘積，同時更新 output
    left_product = 1
    for i in range(n):
        output[i] *= left_product
        left_product *= nums[i]

    # 計算右側乘積，同時將其與 output 相乘得到最終結果
    right_product = 1
    for i in range(n - 1, -1, -1):
        output[i] *= right_product
        right_product *= nums[i]

    return output
