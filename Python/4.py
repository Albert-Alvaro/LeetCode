class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        list1 = nums1
        list2 = nums2
        merged = list1 + list2

        merged.sort()
        length = len(merged)

        if length % 2 == 0:
            median = float((merged[int(length/2)]+merged[int(length/2)-1]))/2
        else:
            median = float(merged[int((length)/2)])

        return median
    
