class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        optimus = []
        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                lower =  j + 1
                upper = len(nums) - 1
                while upper > lower:
                    s = nums[i] + nums[j] + nums[lower] + nums[upper]
                    if s == target:
                    
                        optimus.append([nums[i],nums[j],nums[lower],nums[upper]])
                        lower += 1
                    elif s < target:
                        lower += 1
                    else:
                        upper -= 1
        list1 = list(set(tuple(sorted(sub)) for sub in optimus))
        return list1
                        
                        
