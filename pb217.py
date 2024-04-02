# Given an integer array nums, return true if any value appears at least twice in the array,
# and return false if every element is distinct.


def contains_duplicate(numlist) -> bool:
    return len(set(numlist)) < len(numlist)


nums1 = [1, 2, 3, 1]
nums2 = [1, 2, 3, 4]
nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]


print(contains_duplicate(nums1))
print(contains_duplicate(nums2))
print(contains_duplicate(nums3))
