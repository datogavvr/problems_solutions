class Solution:
    def trap(self, height: List[int]) -> int:
        l_pointer = 0
        r_pointer = len(height) - 1
        l_max = height[l_pointer]
        r_max = height[r_pointer]
        total = 0
        while l_pointer < r_pointer:
            if l_max <= r_max:
                l_pointer += 1
                l_max = max(l_max, height[l_pointer])
                total += l_max - height[l_pointer]
            else:
                r_pointer -= 1
                r_max = max(r_max, height[r_pointer])
                total += r_max - height[r_pointer]
        return total
