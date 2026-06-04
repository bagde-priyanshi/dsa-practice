class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cleaned = ""
        for char in s:
            if char.isalnum():
                cleaned += char.lower()

        cleaned = list(cleaned.strip())

        return cleaned == cleaned[::-1]

solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal; Panama"))
print(solution.isPalindrome("race a car"))
print(solution.isPalindrome(""))
