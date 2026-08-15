class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:


        nums.sort()
        ans = set()

        for i in range(len(nums)):

            for j in range(i+1,len(nums)):
                left = j + 1
                right = len(nums) - 1
                
                while left < right:

                    quad = (nums[i],nums[j],nums[left],nums[right])


                    total = nums[i] +nums[j] + nums[left] + nums[right]

                    if total == target:

                        ans.add(quad)

                        left += 1
                        right -= 1

                    elif total < target:
                        left += 1

                    else:
                        right -= 1

        return list(ans)
        