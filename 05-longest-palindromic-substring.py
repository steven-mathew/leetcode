class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)

        def solve(left, right):
            while left <= right and s[left] == s[right]:
                left -= 1
                right += 1
            return left, right

        best_sz = 0
        best_str = ""

        for parity in (0, 1):
            for mid in range(n):
                left, right = solve(mid, mid + parity)

                sz = right - left - 1

                if sz > best_sz:
                    best_sz = sz
                    best_str = s[left + 1 : right]

        return best_str
