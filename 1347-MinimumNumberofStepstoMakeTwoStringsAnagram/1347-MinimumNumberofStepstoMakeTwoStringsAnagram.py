
        for char in t:
            count_t[ord(char) - ord('a')] += 1

        steps = 0
        for i in range(26):
            steps += abs(count_s[i] - count_t[i])

        return steps // 2
        
"
