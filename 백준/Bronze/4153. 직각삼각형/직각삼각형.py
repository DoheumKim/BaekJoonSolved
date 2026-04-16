import sys

for line in sys.stdin:
    nums = sorted(map(int, line.split()))

    if nums[0] == 0:break 
    elif nums[0]**2 + nums[1]**2 == nums[2]**2:print("right")
    else:print("wrong")

