# 1. 리스트의 삭제
# 내가 푼 풀이

from audioop import reverse
import datetime
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
# strings = input('문자열 입력 : ')
# word = input('단어 입력 : ')

# print(strings.find(word))

# 문자열.index('찾을문자') => 문자의 시작 위치 반환
# 문자열.find('찾을문자') => 문자의 시작 위치 반환. 찾지못하면 -1 리턴

# 31. 파이썬 자료형의 복잡도 -> (3) 찍음

# 32. 문자열 만들기
# s = input().split()
# print(len(s))

# 33. 거꾸로 출력하기
# numbers = list(map(int, input().split()))
# numbers.reverse()
# print(numbers)

# list.reverse() 는 아무값도 반환하지 않고 list값의 순서를 뒤바꿈
# reversed(list)는 순서가 뒤집힌 list를 반환함
# reversed(list)의 반환형은 list가 아니므로 list(reversed(list))로 감싸 형변환을 해야함

# 34. sort 확인하기
# heights = list(map(int, input('키 입력 : ').split()))

# if heights[0] == min(heights) :
#     print('YES')
# else :
#     print('NO')

# 35. Factory 함수 이용하기
# def one(n):
#     def two(num):
#         result = n ** num
#         return result
#     return two


# a = one(2)
# b = one(3)
# c = one(4)
# print(a(10))
# print(b(10))
# print(c(10))

# 36. 구구단
# num = int(input('숫자 입력 : '))

# for i in range(1, 10) :
#     print(num * i, end=' ')

# 37. count 사용하기
# students = list(input().split())
# set_students = set(students)
# dict_answer = {}

# for name in set_students:
#     dict_answer[name] = students.count(name)

# # print(dict_answer)                  # 딕셔너리에서 최대값을 어떻게 출력할꼬
# # print(max(dict_answer.values()))   # max(딕셔너리.values()) : 딕셔너리의 value값들 중 가장 큰 값을 리턴한다.
# print(f'{max(dict_answer, key=dict_answer.get)}(이)가 총 {max(dict_answer.values())}표로 반장이 되었습니다.')

# 38. 호준이의 아르바이트
# scores = list(map(int, input().split()))
# set_scores = set(scores)  # 중복된 점수 없애기
# count = 0  # 사탕 셀 갯수

# for i in range(3):   # 0, 1, 2 => 3위까지만!
#     max_value = max(set_scores)   # 가장 높은 점수
#     # print('최대점수', max_value)
#     count += scores.count(max_value)   # 가장 높은 점수 몇명인지 세=> 다 1등 => count에 추가
#     # print('중간count', count)
#     set_scores.remove(max_value)  # 중복된 값을 제거해줘야 다음 for문에 두번째 높은 숫자를 체크할 수 있음.
#     # print(set_scores)

# print('정답count', count)

# 39. 오타 수정하기
# words = input('문자 입력 : ')
# print(words.replace('q', 'e').replace('b', 'n'))

# 40. 놀이동산에 가자
# limit_weight = int(input())
# n = int(input())
# friends_weights = []

# for _ in range(n):
#     friends_weights.append(int(input()))

# count = 0
# total_weight = 0     # 사람들 무게를 더해가면서, limit를 초과했나 체크할거임

# for i in range(len(friends_weights)) :
#     total_weight += friends_weights[i]   # 맨 앞의 사람 태우기

#     if total_weight > limit_weight :
#         break

#     count += 1

# print(count)

# 41. 소수판별
# n = int(input())
# cnt = 0   # 나눠떨어지는 갯수를 셀 변수

# for i in range(2, n+1):
#     if n % i == 0 :
#         cnt +=1
#     else :
#         continue

# if cnt > 0 or n == 1:
#     print('NO')
# else :
#     print('YES')

# 42. 요일 구하기
# def solution(a, b):
#     print(eng_days[datetime.date(2020, a, b).weekday()])

# a, b = map(int, input().split())
# eng_days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

# solution(a, b )

# 43. 10진수를 2진수로

n = int(input())
secondary_num = ''

while True :
    secondary_num += str(n % 2)
    n = n // 2
    
    if n == 1 :
        secondary_num += '1'
        break


print(secondary_num[::-1])
    