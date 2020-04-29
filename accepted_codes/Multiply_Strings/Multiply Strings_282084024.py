class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 =='0':
            return '0'
        n1 = 0
        for i in range(len(num1)):
            n1 *= 10
            n1 += ord(num1[i]) - ord('0')
        n2 = 0
        for i in range(len(num2)):
            n2 *= 10
            n2 += ord(num2[i]) - ord('0')
        result = n1 * n2
        
        result_str = ''
        while result > 0:
            data = result % 10
            result_str = str(data) + result_str
            result = result // 10
        return result_str
