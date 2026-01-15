class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        t_sorted = "".join(sorted(t))
        s_sorted = "".join(sorted(s))

        return s_sorted == t_sorted