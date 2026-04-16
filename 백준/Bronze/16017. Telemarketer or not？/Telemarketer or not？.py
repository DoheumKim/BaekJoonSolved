import sys

nums = [int(sys.stdin.readline()) for _ in range(4)]
is_telemarketer = (
    (nums[0] == 8 or nums[0] == 9) and
    (nums[3] == 8 or nums[3] == 9) and
    (nums[1] == nums[2])
)

if is_telemarketer:print("ignore")
else:print("answer")