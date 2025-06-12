class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        def status(a, b):   
            return (a & 1) << 1 | (b & 1)  # tạo bitmask từ parity (even/odd) của a và b

        ans = float('-inf')
        n = len(s)

        for ca in '01234':
            for cb in '01234':
                if ca == cb:
                    continue
                print(f"\n=== 🔍 Xét cặp (a='{ca}', b='{cb}') ===")
                
                best = [float('inf')] * 4  # best[bitmask] = min(prev_a - prev_b)
                cnt_a = cnt_b = prev_a = prev_b = 0
                left = -1
                for right in range(n):
                    if s[right] == ca:
                        cnt_a += 1
                    if s[right] == cb:
                        cnt_b += 1
                    
                    # Debug khi mở rộng cửa sổ
                    print(f"[→]left={left}, right={right}, s[right]={s[right]}, cnt_a={cnt_a}, cnt_b={cnt_b}")

                    # Rút gọn cửa sổ nếu đủ dài và đủ b
                    while right - left >= k and (cnt_b - prev_b) >= 2:
                        
                        st = status(prev_a, prev_b)
                        old_best = best[st]
                        best[st] = min(best[st], prev_a - prev_b)
                        if best[st] != old_best:
                            print(f"    💾 best[{st}] cập nhật: {best[st]} (parity a={prev_a%2}, b={prev_b%2})")

                        left += 1
                        if s[left] == ca:
                            prev_a += 1
                        if s[left] == cb:
                            prev_b += 1
                        print(f"    🔁 Shrink left={left}, prev_a={prev_a}, prev_b={prev_b}")

                    # Cập nhật kết quả nếu tìm thấy trạng thái đối xứng
                    st2 = status(cnt_a, cnt_b)
                    target = st2 ^ 2  # đối xứng bit 1 của `a`

                    if best[target] < float('inf'):
                        current_score = cnt_a - cnt_b - best[target]
                        if current_score > ans:
                            print(f"✅ Update ans: {current_score} (cnt_a={cnt_a}, cnt_b={cnt_b}, best[{target}]={best[target]})")
                        ans = max(ans, current_score)

        print("\n🎯 Kết quả cuối cùng:")
        return ans if ans != float('-inf') else -1


# =============================
# 🚀 Test cases
# =============================
sol = Solution()

test_cases = [
    ("12042103", 3),
]

for i, (s, k) in enumerate(test_cases, 1):
    print(f"\n🧪 Test case {i}: s = '{s}', k = {k}'")
    result = sol.maxDifference(s, k)
    print(f"➡️  Output = {result}")
