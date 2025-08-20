n = int(input())
nums = list(map(int, input().split()))
nums.sort()
total = 0

for i in range(n-1):
    print(nums)
    s = nums.pop(0) + nums.pop(0)
    total += 0.05 * s
    n -= 1
    if n == 1:
        break
    else:
        if s > nums[-1]:
            nums.append(s)
        else:
            for j in range(n-1):
                if s <= nums[j]:
                    nums.insert(j, s)
                    break
print("{:.2f}".format(total))


# "{:.2f}".format(5)

# 4
# 10 11 12 13