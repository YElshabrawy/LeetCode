
        for i in range(len(s)):
            if s[i] in char_index_map and char_index_map[s[i]] >= start_index:
                start_index = char_index_map[s[i]] + 1

            char_index_map[s[i]] = i
            max_length = max(max_length, i - start_index + 1)

        start_index = 0
        max_length = 0
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index_map = {}  # Map to store the index of each character
class Solution:
"
