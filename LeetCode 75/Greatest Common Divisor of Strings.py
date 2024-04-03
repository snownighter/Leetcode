def gcdOfStrings(str1: str, str2: str) -> str:
    if str1 + str2 != str2 + str1:  # 檢查兩個字串是否可以由最大公因數重複組成
        return ""
    # 求取兩個字串的長度的最大公因數，即為最大公因數的長度
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    gcd_len = gcd(len(str1), len(str2))
    return str1[:gcd_len]
