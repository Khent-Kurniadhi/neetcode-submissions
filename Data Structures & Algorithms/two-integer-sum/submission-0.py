class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair = {}
        result = []
        
        for i in range(len(nums)):
            difference = target - nums[i]

            if difference not in pair:
                pair.update({nums[i]: i})
            
            else:
                result.append(pair[difference])
                result.append(i)
        return result

