class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        spec=['-','+','=']

        num = str(x)

        if num == '0' or int(num) <= -(2147483648) or int(num) >= (2147483648) or num == '2147483648':
            num = 0
        elif num[0] in spec:
            for i in spec:
                if num[0] == i:
                    num = num[1:]
                    num = num[::-1]
                    num = i+num
                else:
                    continue
        else:
            num = num[::-1]
            while num[0] == '0':
                num = num[1:]

        return int(num)

print(Solution.reverse("", 2147483647))
