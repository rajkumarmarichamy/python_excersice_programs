nums = [1, 1, 2]
nums1 = []

for item in nums:
    if item not in nums1:
        nums1.append(item)

print(nums1)
