class Solution:
    def numTrees(self, n: int) -> int:
# for given n, consider every BST with each number 1 <= i <= (n+1) as the root
# with node i as root, we have (i-1) nodes in left subtree and (n-i) in the right
# if t(n) represents all BSTs, given n, then t(n) = sum of all BSTs with each node as root
# all BSTs with node i as root = t(i-1)t(n-i)
# t(0) = t(1) = 1
# eg: t(2) = t(0)t(1) + t(1)t(0) = 2
#     t(3) = t(0)t(2) + t(1)t(1) + t(2)t(0) = 5
        G = [1, 1] + [0] * n
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                G[i] += G[j - 1] * G[i - j]
        return G[n]
