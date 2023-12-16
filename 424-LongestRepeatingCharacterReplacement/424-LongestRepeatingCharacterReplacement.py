        max_count = 0
        char_count = {}
        start = 0
        for end in range(len(s)):
            char_count[s[end]] = char_count.get(s[end], 0) + 1
            max_count = max(max_count, char_count[s[end]])
            curr_len = end - start + 1
            if curr_len - max_count > k:
                char_count[s[start]] -= 1
                start += 1
            max_length = max(max_length, end - start + 1)
        return max_length

"
