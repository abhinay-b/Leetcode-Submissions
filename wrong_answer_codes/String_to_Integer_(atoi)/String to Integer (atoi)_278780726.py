class Solution:
    def myAtoi(self, a: str) -> int:
        intMax = 2 ** 31 - 1
        intMin = -2 ** 31
        a = a.strip()
        digits = "0123456789"
        if len(a) == 0 or a[0] not in digits:
            return 0
        index = 1
        while a[index] in digits:
            index += 1
            if index == len(a):
                break
        if index > 0:
            a = a[:index]
        
        number = int(a)
        if number > intMax:
            number = intMax
        elif number < intMin:
            number = intMin
        return(number)
