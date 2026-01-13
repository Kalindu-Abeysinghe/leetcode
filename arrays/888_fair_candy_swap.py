class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        """
        :type aliceSizes: List[int]
        :type bobSizes: List[int]
        :rtype: List[int]
        """
        alice_sum = sum(aliceSizes)
        bob_sum = sum(bobSizes) 
        bob_set = set(bobSizes)
        diff = (bob_sum - alice_sum) / 2

        for num in aliceSizes:
            if (diff + num) in bob_set:
                return [num, (diff + num)]

        return []