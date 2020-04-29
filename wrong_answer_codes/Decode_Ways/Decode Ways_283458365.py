class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0
        # s = s.lstrip("0")
        res = []
        res.append([s[0]])
        for char in s[1:]:
            temp = []
            for ele in res:
                # print(ele,char)
                if char == "0":
                    if len(ele[-1]) == 1 and 0 < int(ele[-1]+char) < 27:
                        element=ele.pop(-1)
                        ele.append(element+char)
                        # print(ele)
                    else:
                        return 0
                else:
                    if len(ele[-1]) == 1 and int(ele[-1]+char) < 27:
                        temp.append( ele[:-1]+[ele[-1]+char])
                    ele.append(char)
            res += temp.copy()
            # print(res,temp)
        return len(res)
