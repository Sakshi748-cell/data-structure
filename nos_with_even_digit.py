lass Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0

        for num in nums:

            count = 0

            while num > 0:
                count += 1
                num //= 10

            if count % 2 == 0:
                ans += 1

        return ans