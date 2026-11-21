class Solution:
    def hasDuplicate(self, nums: List[int]):
        num_dict = {}
        for i in nums:
            if i in num_dict:
                num_dict[i] += 1
            else:
                num_dict[i] = 1

        for j in num_dict.values():
            if j != 1:
                return True
        return False