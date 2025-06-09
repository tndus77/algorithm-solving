class Solution:
    def hIndex(self, citations: List[int]) -> int:
        idx = 0  # 기준
        cnt = 0 # 인용된 것들 중 idx 이상인 갯수

        while cnt >= idx:
            cnt = 0
            idx = idx + 1
            for citation in citations:
                if citation >= idx:
                    cnt += 1
        return idx - 1

        