            # base case
            if len(current) == k:
                return output.append(current.copy())
            for i in range(start, n + 1):
                backtrack(current + [i], i + 1)


        backtrack([], 1)
        return output
        output = []
        def backtrack(current: List[int], start: int):
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
4
