class Solution(object):
    def productExceptSelf(self, nums):
        left = []
        right = []
        
        product = 1
        for i in range(0, len(nums)):
            left.append(product)
            product *= nums[i]
        #left[1, a, a*b, a*b*c]
        
        product = 1
        for i in range(len(nums)-1, -1, -1):
            right.append(product)
            product *= nums[i]
        right.reverse()
        #right[b*c*d,c*d,d,1]
        
        for idx in range(len(nums)):
            left[idx] *= right[idx]
        
        return left
            
                
        