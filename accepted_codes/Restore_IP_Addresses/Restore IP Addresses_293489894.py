class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def buildAll(stream,groups,net):
            # print('net',net,stream)
            if not stream and groups == -1:
                res.append(net[:-1])
                return
            elif not stream or groups == -1:
                return
            temp = stream[0]
            stream = stream[1:]
            m = len(stream)
            while len(temp) < 4 and groups <= m:
                # print('temp',temp)
                buildAll(stream,groups-1,net+temp+'.')
                if not stream or temp == '0' or int(temp+stream[0]) > 255:
                    break
                temp += stream[0]
                stream = stream[1:]
                m -= 1                

            if m > groups*3:
                    return
        res = []
        buildAll(s,3,'')
        return res
        
