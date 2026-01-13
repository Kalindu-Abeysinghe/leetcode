class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        smaller_arr = nums1 if len(nums1) <= len(nums2) else nums2
        larger_arr = nums1 if len(nums1) > len(nums2) else nums2
        intersection = set(larger_arr)

        for num in intersection.copy():
            if num not in smaller_arr:
                intersection.remove(num)
        
        return list(intersection)