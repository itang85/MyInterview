def find_num_N(nums):
    digit = 3
    num1 = nums[0]
    num2 = nums[1]
    num3 = nums[2]
    while True:
        num = num1 + num2 + num3
        if num > 10:
            digit += 2
            num1 = num3
            num2 = int(num / 10)
            num3 = num % 10
        else:
            digit += 1
            num1 = num2
            num2 = num3
            num3 = num
        if digit == nums[-1]:
            return num3
        if digit > nums[-1]:
            return num2


howmany = int(input())
nums_list = []
for i in range(howmany):
    nums_list.append(list(map(int, input().split())))
for n in nums_list:
    print(find_num_N(n))
