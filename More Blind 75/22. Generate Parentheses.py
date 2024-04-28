class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        '''
        res = []

        def combination(stack, temp, parentheses, num):

            if parentheses == '(':
                if num[0] == 0:
                    return
                num[0] -= 1
                stack.append(parentheses)
            elif parentheses == ')':
                if num[1] == 0:
                    return
                if not stack:
                    return
                num[1] -= 1
                stack.pop()

            temp.append(parentheses)
            if num[0] == 0 and num[1] == 0:
                res.append(''.join(temp))
                return

            combination(stack.copy(), temp.copy(), '(', num.copy())
            combination(stack.copy(), temp.copy(), ')', num.copy())

        combination([], [], '(', [n,n])

        return res
        '''

        def backtrack(current, left, right):
            if len(current) == 2 * n:
                result.append(current)
                return
            if left < n:
                backtrack(current + '(', left + 1, right)
            if right < left:
                backtrack(current + ')', left, right + 1)

        result = []
        backtrack('', 0, 0)
        return result
