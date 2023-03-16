
from pip import List
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:    
        self.quickSort(nums, 0, len(nums) - 1)
        return nums
        
    def quickSort(self, nums:List[int], left:int, right:int ) -> None:
        if left >= right:
            return
        p = self.partition(nums, left, right)
        self.quickSort(nums, left, p - 1)
        self.quickSort(nums, p + 1, right)

    def partition(self, nums:List[int], left:int, right:int) -> int:
        i = left
        j = right
        pivot = nums[left]
        while i != j:
            while nums[j] >= pivot and i < j:
                j -= 1
            while nums[i] <= pivot and i < j:
                i += 1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
        nums[left] = nums[i]
        nums[i] = pivot
        print(nums)
        return i
 
if __name__ == '__main__':
    s = Solution()
    arr = [5,2,3,1,37,87,3,6,890]
    s.sortArray(arr)
