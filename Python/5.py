class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        strings = s
        strs = []
        max = 0

        length = len(strings)
        for i in range(1,length+1):
            for j in range(0, length):
                strs.append(strings[j:i])
                if strings[j:i] == '':
                    strs.remove('')
        for s in strs:
            if s == s[::-1] and max < len(s):
                max = len(s)
                result = s
        return result


print(Solution.longestPalindrome("","cbbd"))