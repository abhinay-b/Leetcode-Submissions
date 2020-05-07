class Solution:
    def countAndSay(self, n: int) -> str:
        def count(stack):
            tmp_stack = []
            ret = []
            for elem in stack:
                try:
                    if tmp_stack[-1][0] == elem:
                        count = tmp_stack.pop()[1]
                        tmp_stack.append((elem, count + 1))
                    else:
                        tmp_stack.append((elem, 1))
                except IndexError:
                    tmp_stack.append((elem, 1))

            for elem in tmp_stack:
                ret.append(elem[1])
                ret.append(elem[0])

            return ret

        if n == 1:
            return '1'

        stack = [1]
        new_stack = []

        for _ in range(n - 1):
            new_stack = count(stack)
            stack = new_stack

        return ''.join(map(str,new_stack))
