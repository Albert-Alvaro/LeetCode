class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        strings = s
        strs = []
        max = 0

        # length = len(strings)
        # for i in range(1,length+1):
        #     for j in range(0, length):
        #         strs.append(strings[j:i])
        #         if strings[j:i] == '':
        #             strs.remove('')
        # for s in strs:
        #     if s == s[::-1] and max < len(s):
        #         max = len(s)
        #         result = s
        # return result
        if Solution.is_palindrome(s):
            return s

        maxp = s[0]

        for i in range(len(s)-1):
            half_length = len(maxp) // 2
            start = i - half_length
            end = i + half_length

            while start >= 0 and end <= len(s)-1:
                if Solution.is_palindrome(s[start:end+2]):
                    if len(s[start:end+2]) > len(maxp):
                        maxp = s[start:end+2]
                    end += 1
                elif Solution.is_palindrome(s[start:end+1]):
                    if len(s[start:end+1]) > len(maxp):
                        maxp = s[start:end+1]
                    start -= 1
                    end += 1
                else:
                    break

        return maxp
    def is_palindrome(s):
        return s == s[::-1]


print(Solution.longestPalindrome("","civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"))