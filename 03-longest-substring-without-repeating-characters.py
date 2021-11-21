from collections import deque


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        window = set()

        left = 0
        right = 0
        ans = 0

        while right < len(s):
            if s[right] in window:
                window.remove(s[left])
                left += 1
            else:
                window.add(s[right])
                right += 1

            ans = max(ans, right - left)
        return ans

        ###

        count = {}
        left = 0
        ans = 0

        for right, c in enumerate(s):
            if c in count:
                left = max(left, count[c] + 1)
            ans = max(ans, right - left + 1)
            count[c] = right

        return ans
