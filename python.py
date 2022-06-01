# 1. 리스트의 삭제
# 내가 푼 풀이
from audioop import reverse


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
for i in range(1, n+1):
    print(' '*(n-i) + '*'*(2*i-1))

# 11. for를 이용한 기본 활용
s = 0

for i in range(1, 101):
    s += i

print(s)

# 정답코드
# for i in range(101):
#     s+=i

# 12. 게임 캐릭터 클래스 만들기


class Wizard:
    # 속성 생성
    def __init__(self, health, mana, armor):
        self.health = health
        self.mana = mana
        self.armor = armor

    # 메소드 생성
    def attack(self):
        print('파이어볼')


x = Wizard(health=545, mana=210, armor=10)
print(x.health, x.mana, x.armor)
x.attack()

# 13. 몇번째 행성인가요?
# universe = ['수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성']
# print(universe[int(input('인덱스입력:'))-1])

# 14. 3의 배수인가요?
# a = int(input('숫자 입력 : '))

# if a % 3 == 0 :
#     print('짝')
# else :
#     print(a)

# 15. 자기소개
# b = input('이름입력 : ')
# print(f'안녕하세요. 저는 {b}입니다.')

# 16. 로꾸거
b = '안녕하세요'
print(b[::-1])

# 17. 놀이기구 키제한
# c = int(input('키 입력 : '))
# if c >= 150 :
#     print('YES')
# else :
#     print('NO')

# 18. 평균 점수
# scores = list(map(int, input('점수입력 : ').split(' ')))
# print(int(sum(scores)/len(scores)))

# 19. 제곱을 구하자
# nums = list(map(int, input('두수입력 : ').split(' ')))
# print(nums[0]**nums[1])

# 20. 몫과 나머지
# nums2 = list(map(int, input().split()))
# 몫 = nums2[0] // nums2[1]
# 나머지 = nums2[0] % nums2[1]

# print(몫, 나머지)

# 21. set은 어떻게 만드나요? => 3번. : 틀림 정답은 x={} => 딕셔너리임.
# x = set('python')
# print(x)  => set 선언하는 방법. 출력값은 {'o', 'h', 'n', 't', 'y', 'p'}
# 1. fruits = {'strawberry', 'grape', 'orange', 'pineapple', 'cherry'}
# 2.  a = set('apple')
# 3.  c = set()
# 아닌 경우 =>  c = {}
# print(type(c))   => dict형으로 나온다.

# 22. 배수인지 확인하기 => 2번.
# 23. OX문제 => 5.0이다.

# 24. 대문자로 바꿔주세요.
# a = input().upper()
# print(a)

# 25. 원의 넓이 구하기
# def circle_area(r) :
#     return r*r*3.14

# a = int(input())
# print(circle_area(a))

# 26. 행성문제2
# planets = {
#     '수성' : 'Mercury',
#     '금성' : 'Venus',
#     '지구' : 'Earth',
#     '화성' : 'Mars',
#     '목성' : 'Jupiter',
#     '토성' : 'Saturn',
#     '천왕성' : 'Uranus',
#     '해왕성' : 'Neptune',
#     }

# print(planets[input()])

# 27. 딕셔너리 만들기
# 내가 푼 풀이
# names = input('이름 : ').split(' ')
# scores = input('수학점수 :').split(' ')

# dic = {}
# for i in range(len(names)) :
#     dic[names[i]] = int(scores[i])

# print(dic)

# 정답 풀이
# keys = input().split()
# values = map(int, input().split())

# result = dict(zip(keys, values))
# print(result)

# d = dict(zip(['a,b,c'], [1,2,3]))  # 키는 키끼리, 값은 값끼리 묶어서 zip함수에 전달해서 딕셔너리를 생성한다.

# 28. 2-gram
# s = input()

# for i in range(len(s)-1):   # 마지막 for문은 돌면 범위에서 벗어났다고 에러발생.
#     print(s[i] + s[i+1])

# 29. 대문자만 지나가세요
# s = input('알파벳 입력 : ')

# if s == s.upper():
#     print('YES')
# else :
#     print('NO')
    
# long_s = input('알파벳여러개입력 : ')

# result = ''

# for i in range(len(long_s)):
#     if long_s[i] == long_s[i].upper():
#         result += long_s[i]

# print(result)
        
# 30. 문자열 속 문자찾기
strings = input('문자열 입력 : ')
word = input('단어 입력 : ')

print(strings.find(word))

# 문자열.index('찾을문자') => 문자의 시작 위치 반환
# 문자열.find('찾을문자') => 문자의 시작 위치 반환. 찾지못하면 -1 리턴
