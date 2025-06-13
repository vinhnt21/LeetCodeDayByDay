from typing import List

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()  # Bước 1: Sắp xếp để độ chênh lệch nhỏ nằm gần nhau
        print(f"Sorted nums: {nums}")
        def can_form_p_pairs(max_diff):
            count = 0
            i = 0
            while i < len(nums) - 1:
                print(f"count: {count}, i: {i}, checking pair: ({nums[i]}, {nums[i + 1]}) with max_diff: {max_diff}")
                if nums[i + 1] - nums[i] <= max_diff:
                    count += 1
                    i += 2  # bỏ cả 2 phần tử vì mỗi phần tử chỉ dùng 1 lần
                else:
                    i += 1  # không ghép được thì chỉ bỏ 1 phần tử
            print(f"Total pairs formed: {count}")
            return count >= p

        # Bước 2: Tìm kiếm nhị phân trên đáp án
        left, right = 0, nums[-1] - nums[0]
        print(f"Initial left: {left}, right: {right}")
        answer = right

        while left <= right:
            mid = (left + right) // 2
            print(f"Current left: {left}, right: {right}", f", mid: {mid}")
            
            if can_form_p_pairs(mid):
                answer = mid
                right = mid - 1  # thử tìm giá trị nhỏ hơn
            else:
                left = mid + 1  # phải tăng độ chênh lệch lên

        return answer

nums = [1,5,2,3]
p = 2
solution = Solution()
print(solution.minimizeMax(nums, p))  # Output: 1