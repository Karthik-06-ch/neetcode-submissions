class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
      nums1 = nums
      if len(set(nums)) == len(nums1):
        return False
      else:
        return True
      
      
       #n = len(nums)
        #for i in range(n):
         #   for j in range(n):
          #      if nums[i] == nums[j]:
           #         return True
            #    else:
             #       return False###