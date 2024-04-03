def mergeAlternately(word1: str, word2: str) -> str:
    result = ""
    i, j = 0, 0
    while i < len(word1) and j < len(word2):
        result += word1[i]
        result += word2[j]
        i += 1
        j += 1
    result += word1[i:]  # 將 word1 中剩餘的字元添加到結果中
    result += word2[j:]  # 將 word2 中剩餘的字元添加到結果中
    return result
