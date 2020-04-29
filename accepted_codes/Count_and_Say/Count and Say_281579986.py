class Solution:
    def countAndSay(self, n: int) -> str:
        string = '1'
        for _ in range(1,n):
            new_string = ''
            prev_char = ''
            count = 0
            for char in string:
                if char == prev_char:
                    count += 1
                else:
                    if count > 0:
                        new_string += str(count) + prev_char
                    prev_char = char
                    count = 1
            new_string += str(count) + prev_char
            string = new_string
        return string
        
        
        return string
