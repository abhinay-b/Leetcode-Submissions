class Solution:
    def myAtoi(self, a: str) -> int:
        intMax = 2 ** 31 - 1
        intMin = -2 ** 31
        a = a.strip()
        digits = "0123456789"
        if len(a) == 0 or a[0] not in (digits+'-'):
            return 0
        index = 1
        while index < len(a) and a[index] in digits:
            index += 1
        if index > 0:
            a = a[:index]
        if a == '-':
            return 0
        number = int(a)
        if number > intMax:
            number = intMax
        elif number < intMin:
            number = intMin
        return(number)
