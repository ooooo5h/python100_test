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
n = 10
b = 2
for i in range(1, 5, 2):  # (1,3)
    n += i   # i가 1일때 a = 10 + 1 = 11.
    # i가 3일때 a = 11 + 3 = 14.
print(n+b)   # 14 + 2 = 16. 정답 4번

# 6. false => 2
# 7. 변수명 => 4,5  땡!!!! _age는 가능하다.
# 파이썬의 변수명 => 영문문자와 숫자 사용 가능, 문자부터 시작해야한다(숫자시작 불가능!!), 밑줄로 시작할 수 있다.
# as가 안되는 이유 => 예약어는 파이썬 변수명으로 사용 불가하다.

# 8. 딕셔너리 키 이름 중복
d = {'height': 180, 'weight': 78, 'weight': 84, 'temparture': 36, 'eyesight': 1}
print(d['weight'])     # 78 출력   => 땡!!!
# 딕셔너리는 키 이름의 중복을 허용하지 않아서 덮어쓴다.
# 따라서 가장 마지막 값인 84가 출력된다.
# print(d)

# 9. sep과 end를 활용한 출력방법
year = '2019'
month = '04'
day = '26'
hour = '11'
minute = '34'
second = '27'

print(year, month, day, sep='/', end=' ')
print(hour, minute, second, sep=':')

# sep='?' : 값 사이에 공백이 아닌 문자를 넣고 싶을 때 사용한다.

# 10. 별찍기
# n = int(input())
for i in range(1, n+1) :
    print(' '*(n-i) + '*'*(2*i-1))
    
# 11. for를 이용한 기본 활용
s = 0

for i in range(1, 101) :
    s += i

print(s)

# 정답코드
# for i in range(101):
#     s+=i

# 12. 게임 캐릭터 클래스 만들기
class Wizard :
    # 속성 생성
    def __init__(self, health, mana, armor):
        self.health = health
        self.mana = mana
        self.armor = armor
        
    # 메소드 생성
    def attack(self):
        print('파이어볼')


x = Wizard(health = 545, mana = 210, armor = 10)
print(x.health, x.mana, x.armor)
x.attack()

# 13. 몇번째 행성인가요?
universe = ['수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성']
print(universe[int(input('인덱스입력:'))-1])