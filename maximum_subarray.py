class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #nums = [-2,3,2,-1]
        max_i = [0]*len(nums)
        max_j = [0]*len(nums)
        max_val = nums[0]
        sum_arr = [0]*len(nums)
        sum_arr[0] = max_val
        for i in range(1,len(nums)):
            if (sum_arr[i-1]+nums[i])>nums[i]:
                max_j[i] = i
                sum_arr[i] = sum_arr[i-1]+nums[i]
            else:
                max_i[i] = i
                sum_arr[i] = nums[i]
            max_val = max(max_val,sum_arr[i])
            max_j[i]=1
            
        #print(sum_arr)
        #print(max_val)
        return max_val