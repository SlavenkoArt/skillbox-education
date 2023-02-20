def add_num(num, nums = []):
    nums.append(num)
    print(nums)

add_num(5)
add_num(10)
add_num(15)

def add_num2(num, nums = None):
    nums = nums or []
    if not nums:
        nums = []
    nums.append(num)
    print(nums)

add_num2(5)
add_num2(10)
add_num2(15)