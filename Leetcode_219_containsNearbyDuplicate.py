class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        # using dictionary
        # nums_dict = {}
        # for i in range(len(nums)):
        #     try:
        #         nums_dict[nums[i]].append(i)
        #     except KeyError:
        #         nums_dict[nums[i]] = [i]
        # for key in nums_dict:
        #     for i in range(len(nums_dict[key])-1):
        #         if abs(nums_dict[key][i] - nums_dict[key][i+1]) <= k:
        #             return True
        # return False

        # Using set
        window = set()
        L = 0
        for R in range(len(nums)):
            if R - L > k:
                window.remove(nums[L])
                L += 1
            if nums[R] in window:
                return True
            else:
                window.add(nums[R])
                R += 1
        return False


sol = Solution()
print(sol.containsNearbyDuplicate(nums = [2,2], k = 3))



