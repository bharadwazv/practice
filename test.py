class Solution:
    def maxScore(self, c: List[int], k: int) -> int:
        i=0
        j=len(c)-k
        s=sum(c[i:j])
        res=s
        for _ in range(k):
            s -= c[i]
            s += c[j]
            i += 1
            j += 1
            res = min(res, s)
        return sum(c)-res
