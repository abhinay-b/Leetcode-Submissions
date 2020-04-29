class Solution:
    def countAndSay(self, n: int) -> str:
        if n < 1:
            return ""
        freq = ctr = 1
        nxt_seq = "1"
        while ctr < n:
            length = 0 
            seq = nxt_seq
            nxt_seq = ""
            while 1:
                freq = 1
                while (length < len(seq) - 1) and (seq[length] == seq[length+1]):
                    freq += 1
                    length += 1
                nxt_seq += str(freq) + seq[length]
                if length < len(seq) - 1:
                    length += 1
                else:
                    break
            ctr += 1
        return nxt_seq
