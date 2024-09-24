#Contains Duplicate - Easy

class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        hashSet=set()
        for i in nums: #checks all the values in nums list
            if i in hashSet: #every value gets checked to see if it is in the set already
                return True #returns true if duplicate
            hashSet.add(i) #every value gets added into set so the if statement can check if dups
        return False
            
if __name__ == '__main__':
    
    nums=[1,2,3,3]
    solution = Solution()

    result = solution.hasDuplicate(nums)
    print(result)