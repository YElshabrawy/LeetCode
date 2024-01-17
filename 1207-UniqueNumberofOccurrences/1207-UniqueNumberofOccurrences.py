class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        occur = Counter(arr).values()
        return len(occur) == len(set(occur))
[
