'''
Idea here is to identify
1. Divide the list into two sorted lists. 
2. check if the mid item is greater than the left item then left hand side of the list is sorted otherwise right hand side. 
3. Now check if the target item is greater than left item and less than mid item. then adjust right to mid - 1 
4. same for right hand side
overall it is divide list into two lists and apply binary search on both sides separately

'''


def rotated_search(nums, target):
    left, right = 0, len(nums) - 1


    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[left] <=nums[mid]:
            if nums[left] <= target and nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target and target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

nums = [6,7,8,0,1,2,3,4,5]
target = 6
print(rotated_search(nums, target))
