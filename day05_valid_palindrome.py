# Two Pointer method using in-built python string manipulation and class
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

# Two Pointer Method for Palindrome checking in a string using While Loop

string = "racecar"
string = string.lower()

left = 0
right = len(string) - 1
is_palindrome = True

while left < right:
    if string[left] != string[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1

if is_palindrome:
    print(f"{string} is a palindrome")
else:
    print(f"{string} is not a palindrome")

