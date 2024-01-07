                    continue

                count = dp[j][diff] if diff in dp[j] else 0

                # Add the count to the total and update dp[i][diff]
                total_count += count
                dp[i][diff] += count + 1

        return total_count
[
