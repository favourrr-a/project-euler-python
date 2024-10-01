nums = [1 for i in range(2000000)]
nums[0] = nums[1] = 0

for i in range(2, int(len(nums) ** 0.5) + 1):
    if nums[i] == 1:
        for j in range(i * i, len(nums), i):
            nums[j] = 0
    else:
        continue

print(sum([x for x in range(2, len(nums)) if nums[x] == 1]))