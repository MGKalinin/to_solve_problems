from typing import List

#3Sum
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #nums[i] + nums[l] + nums[r] = 0
        nums.sort()#сортировка списка
        ans = []#здесь ответы
        for i in range(len(nums)-1):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            l,r = i + 1,len(nums)-1#l = i + 1
            while l<r:
                if nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    ans.append([nums[i] ,nums[l], nums[r]])#сдвинуть оба указателя внутрь
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        return ans


nums = [-1,0,1,2,-1,-4]
print(Solution().threeSum(nums))
