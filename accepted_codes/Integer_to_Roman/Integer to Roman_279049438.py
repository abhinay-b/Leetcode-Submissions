class Solution:
    def intToRoman(self, num: int) -> str:
        hashmap = {1:"I", 4:"IV", 5:"V", 9:"IX", 10:"X", 40:"XL", 50:"L", 90:"XC", 100:"C", 
            400:"CD", 500:"D", 900:"CM", 1000:"M"}
        res = ""
        div = 1000
        while num > 0:
            quo = num // div
            prod = quo * div
            if prod in hashmap:
                res += hashmap[prod]
            elif quo < 5:
                res += quo * hashmap[div]
            else:
                res += hashmap[5*div] + (quo-5)*hashmap[div]
            num = num % div
            div //= 10
        return res
