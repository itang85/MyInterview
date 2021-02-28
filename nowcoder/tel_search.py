import re
nums = list(map(int, input().split()))
phones = [input() for i in range(nums[0])]
strs = [input() for i in range(nums[1])]

for s in strs:
    times = 0
    for p in phones:
        if re.search(s, p):
            times += 1
    print(times)
