# 1. 리스트의 삭제
# 내가 푼 풀이
nums = [100, 200, 300, 400, 500]
nums.remove(400)
nums.remove(500)
print(nums)

# 답안 풀이
nums1 = [100, 200, 300, 400, 500]
nums1.pop()
nums1.pop()
print(nums1)

# 2. 리스트의 내장함수
l = [200, 100, 300]
l.insert(2, 10000)
print(l)

# 3. 변수의 타입 => 정답 3번 리스트.

# 4. 변수의 타입2 => 정답 3번. 출력값이 str.

# 5. for문 계산
a = 10
b = 2
for i in range(1, 5, 2):  # (1,3)
    a += i   # i가 1일때 a = 10 + 1 = 11.
             # i가 3일때 a = 11 + 3 = 14.
print(a+b)   # 14 + 2 = 16. 정답 4번

# 6. false => 2