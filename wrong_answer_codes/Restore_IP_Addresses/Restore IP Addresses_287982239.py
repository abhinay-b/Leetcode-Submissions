class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def buildAll(stream,groups,net):
            if not stream and groups == -1:
                res.append(net[:-1])
                return
            elif not stream or groups == -1:
                return
            temp = stream[0]
            stream= stream[1:]
            m = len(stream)
            while m > groups*3:
                temp += stream[0]
                stream = stream[1:]
                m -= 1
                if len(temp) == 2 and int(temp[0]) > 2:
                    if m > groups*3:
                        return
                    else:
                        break
                elif len(temp) == 3 and m > groups*3:
                    return
            while len(temp) < 4:
                buildAll(stream,groups-1,net+temp+'.')
                if not stream:
                    break
                if len(temp) == 2 and int(temp[0]) > 2:
                    break
                temp += stream[0]
                stream = stream[1:]
        res = []
        buildAll(s,3,'')
        return res
        
