# print(5)
# print(-10)
# print(3.14)
# print(1000)
# print(5+3)
# print(2*8)
# print(3*(3+1))

# print('풍선')
# print("나비")
# print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
# print("ㅋ"*9)

# boolean
# print(5 > 10)
# print(5<10)
# print(True)
# print(False)
# print(not True)
# print(not False)
# print(not (5 > 10))

# 애완동물을 소개해 주세요~
# animal = "고양이"
# name = "해피"
# age = 4
# hobby = "낮잠"
# is_adult = age >= 3

# print("우리집 " + animal + "의 이름은 " + name +"예요")
# hobby = "공놀이"
# # print(name + "는 " + str(age) +"살이며, " + hobby +"를 아주 좋아합니다")
# print(name, "는 ", age, "살이며, ", hobby, "를 아주 좋아합니다")
# print(name + "는 어른일까요? " + str(is_adult))

'''
Quiz) 변수를 이용하여 다음 문장을 출력하시오

변수명
 : Station

변수값
 : "사당", "신도림", "인천공항" 순서대로 입력

출력 문장
 : XX행 열차가 들어오고 있습니다.

station = "사당"
print(station + "행 열차가 들어오고 있습니다.")
'''
#연산자

# print(1+1)
# print(3-2)
# print(5*2)
# print(6/3)

# print(2**3)
# print(5%3)
# print(10%3)
# print(5//3)
# print(10//3)

# print(10 > 3)
# print(4 >= 7)
# print(10 < 3)
# print(5 <=5)

# print(3 == 3)
# print(4 == 2)
# print(3 + 4 == 7)

# print(1 != 3)
# print(not(1 != 3))

# print((3 > 0) and (3 < 5))
# print((3 > 0) & (3 < 5))

# print((3 > 0) or (3 > 5))
# print((3 > 0 ) | ( 3 > 5))

# print(5 > 4 > 3)
# print(5 > 4 > 7)

#수식
# print(2 + 3 * 4)
# print((2+3) * 4)
# number = 2 + 3 * 4
# print(number)
# number = number + 2
# print(number)
# number += 2
# print(number)
# number *=2
# print(number)
# number /= 2
# print(number)
# number -= 2
# print(number)

# number %= 5
# print(number)

# print(abs(-5))
# print(pow(4, 2))
# print(max(5, 12))
# print(min(5, 12))
# print(round(3.14))
# print(round(4.99))

from math import *
from operator import sub
from os import name, rename, scandir

# print(floor(4.99))
# print(ceil(3.14))
# print(sqrt(16))

from random import *
# print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
# print(random()* 10)
# print(int(random() * 10))
# print(int(random() * 10) + 1)

# print(int(random()*45)+1)
# print(int(random()*45)+1)
# print(int(random()*45)+1)
# print(int(random()*45)+1)
# print(int(random()*45)+1)
# print(int(random()*45)+1)

# print(randrange(1, 46))
# print(randrange(1, 46))
# print(randrange(1, 46))
# print(randrange(1, 46))
# print(randrange(1, 46))
# print(randrange(1, 46))

# print(randint(1, 45))
# print(randint(1, 45))
# print(randint(1, 45))
# print(randint(1, 45))
# print(randint(1, 45))
# print(randint(1, 45))

'''
Quiz) 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으롷기로 했습니다.
아래 조건에 맞는오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.

조건1 : 핸덤으로 날짜를 뽑아야 함
조건2 : 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
조건3 : 매월 1~3일은 스터디 준비를 해야하므로 제외

(출력문 예제)
오프라인 스터디모임 날짜는 매월 x 일로 선정 되었습니다.

date = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월 " + str(date) + "일로 선정되었습니다.")
'''

# sentence = '나는 소년입니다.'
# print(sentence)
# sentence2 = "파이썬은 쉬워요"
# print(sentence2)
# sentence3 = """
# 나는 소년이고,
# 파이썬은 쉬워요
# """
# print(sentence3)

# jumin = "990120-1234567"

# print("성별 : " + jumin[7])
# print("연 : " + jumin[0:2]) # 0부터 2직전까지
# print("월 : " + jumin[2:4])
# print("일 : " + jumin[4:6])

# print("생년월일 : " + jumin[:6])
# print("뒤 7자리 : " + jumin[7:])
# print("뒤 7자리 (뒤에부터) : " + jumin[-7:])

# python = "Python is Amazing"
# print(python.lower())
# print(python.upper())
# print(python[0].isupper())
# print(len(python))
# print(python.replace("Python", "Java"))

# index = python.index("n")
# print(index)
# index = python.index("n", index + 1)
# print(index)

# print(python.find("Java")) # find는 원하는값이 없을때 -1 출력
# # print(python.index("Java")) # index는 원하는 값이 없을때 오류

# print(python.count("n"))

# print("a" + "b")
# print("a", "b")

#방법1
# print("나는 %d살입니다." % 20) #d는 항상 정수
# print("나는 %s을 좋아해요" % "파이썬")
# print("Apple 은 %c로 시작해요." % "A") #c는 한 글자만 가능
# # %s로쓰면 구분없이 전부 가능하다
# print("나는 %s살입니다." %20)
# print("나는 %s색과 %s색을 좋아해요" % ("파랑", "빨강"))

#방법2
# print("나는 {}살입니다.".format(20))
# print("나는 {1}색과 {0}색을 좋아해요.".format("파랑", "빨강"))

#방법3
# print("나는 {age}살이며, {color}색을 좋아해요.".format(age =20, color ="빨강"))

#방법4
# age = 20
# color = "파랑"
# print(f"나는 {age}살이며, {color}색을 좋아해요.")

# print("백문이 불여일견 \n백견이 불여일타")
# print('저는 "나도코딩"입니다.')
# print("저는 \"나도코딩\"입니다.")

# \\ : 문장 내에서 \
# print("C:\\Users\\skxog\\Desktop\\PythonWorkSpace")

#\r : 커서를 맨 앞으로 이동
# print("Red Apple \rPine") #덮어쓰기가 적용됨

#\b : 백스페이스 (한 글자 지우기)
# print("Redd\bApple")

#\t = 탭
# print("Red\tApple")

'''
Quiz) 사이트별로 비밀번호를 만들어주는 프로그램을 작성하시오

예) http://naver.com
규칙1 : http:// 부분은 제외 => naver.com
규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성
예) 생성된 비밀번호 nav51!

address = "http://google.com"
mod = address.replace("http://", "")
mod = mod[:mod.index(".")]
# print(mod)
result = mod[:3] + str(len(mod)) + str(mod.count("e")) + "!"
print("{0} 의 비밀번호는 {1} 입니다.".format(address, result))
'''

#리스트[]
#지하철 칸별로 10명, 20명, 30명
# subway1 = 10
# subway2 = 20
# subway3 = 30

# subway = [10, 20, 30]
# print(subway)

# subway = ["유재석", "조세호", "박명수"]
# print(subway)

# #조세호씨가 몇 번째 칸에 타고있나요?
# print(subway.index("조세호"))

# #하하씨가 다음 정류장에서 다음 칸에 탐
# subway.append("하하")
# print(subway)

# #정형도씨를 유재석과 조세호 사이에 태우기
# subway.insert(1, "정형돈")
# print(subway)

# #지하철에 있는 사람을 한명씩 뒤에서 꺼내기
# print(subway.pop())
# print(subway)

# print(subway.pop())
# print(subway)

# print(subway.pop())
# print(subway)

# #같은 이름의 사람이 몇 명 있는지 확인
# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))

# #정렬도 가능
# num_list = [5,4,3,2,1]
# num_list.sort()
# print(num_list)

# #순서 뒤집기
# num_list.reverse()
# print(num_list)

# #모두 지우기
# num_list.clear()
# print(num_list)

#다영한 자료형 함께사용
# num_list = [5,2,4,3,1]
# mix_list = ["조세호", 20, True]
# print(mix_list)

# #리스트 확장
# num_list.extend(mix_list)
# print(num_list)

# cabinet = {3:"유재석", 100:"김태호"}
# print(cabinet[3])
# print(cabinet[100])

# print(cabinet.get(3))
# # print(cabinet[5])
# print(cabinet.get(5))
# print(cabinet.get(5, "사용 가능"))

# print(3 in cabinet)
# print(5 in cabinet)

# cabinet = {"A-3":"유재석", "B-100":"김태호"}
# print(cabinet["A-3"])
# print(cabinet["B-100"])

# #새 손님
# print(cabinet)
# cabinet["A-3"] = "김종국"
# cabinet["C-20"] = "조세호"
# print(cabinet)

# #간 손님
# del cabinet["A-3"]
# print(cabinet)

# #key 들만 출력
# print(cabinet.keys())

# #value들만 출력
# print(cabinet.values())

# #key, value 둘다
# print(cabinet.items())

# #목욕당 폐점
# cabinet.clear()
# print(cabinet)

# menu = ("돈까스", "치즈까스")
# print(menu[0])
# print(menu[1])

# menu.add("생선까스")

# name = "김종국"
# age = "20"
# hobby = "코딩"
# print(name, age, hobby)

# name, age, hobby = "김종국", 20, "코딩"
# print(name, age, hobby)

# #집합(set)
# #중복 안됨, 순서 없음
# my_set = {1,2,3,3,3}
# print(my_set)

# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석", "박명수"])

# #교집합 (java와 python을 모두 할 수 있는 개발자)
# print(java & python)
# print(java.intersection(python))

# #합집합 (java도 할 수 있거나 python도 할 수 있는 개발자)
# print(java | python)
# print(java.union(python))

# #차집합 (java는 할 수 있지만 python은 할 줄 모르는 개발자)
# print(java - python)
# print(java.difference(python))

# #python을 할 줄 아는 사람이 늘어남
# python.add("김태호")
# print(python)

# # java를 잊었어요
# java.remove("김태호")
# print(java)

# #자료구조의 변경
# #커피숍
# menu = {"커피", "우유", "주스"}
# print(menu, type(menu))

# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu, type(menu))

# menu = set(menu)
# print(menu, type(menu))

'''
Quiz) 당신의 학교에서는 파이썬 코딩대회를 주최합니다.
참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.

조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
조건3 : random 모듈의 shuffle과 sample을 활용

(출력 예제)
--당첨자 발표--
치킨 당첨자 : 1
커피 당첨자 : [2, 3, 4]
--축하합니다--
'''

# # (활용 예제)
# from random import *
# # lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# lst = range(1, 21) # 1부터 20까지 생성 단, type이 range로 가기때문에 변경해야함
# lst = list(lst)
# # print(lst)
# shuffle(lst)
# # print(lst)
# # print("---당첨자 발표--- \n치킨 당첨자 : " + str(lst[0]) + "\n커피 당첨자 : " + str(lst[1]) + ", " + str(lst[2]) + ", " + str(lst[3]) + "\n--축하합니다--")
# # print("---당첨자 발표--- \n치킨 당첨자 : " + str(sample(lst, 1)) + "\n커피 당첨자 : " + str(sample(lst, 3)) + "\n--축하합니다--")

# winners = sample(lst, 4)

# print("---당첨자 발표---")
# print("치킨 당첨자 : {0}".format(winners[0]))
# print("커피 당첨자 : {0}".format(winners[1:]))
# print("---축하합니다---")

# #분기처리 (if문)
# weather = input("오늘 날씨는 어때요? ")
# if weather == "비" or "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요")

# temp = int(input("기온은 어때요? "))
# if 30 <= temp:
#     print("너무 더워요. 나가지 마세요")
# elif 10 <= temp and temp < 30:
#     print("괜찮은 날씨에요")
# elif 0 < temp and temp < 10:
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요. 나가지 마세요")

#반복문 (for)
# print("대기번호 : 1")
# print("대기번호 : 2")

# for waiting_no in range(1, 6):
#     print("대기번호 : {0}".format(waiting_no))

# starbucks = ["아이언맨", "토르", "아이엠 그루트"]
# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다.".format(customer))

#반복문 (while)
# customer = "토르"
# index = 5
# while index >=1:
#     print("{0}, 커피가 준비 되었습니다" "{1} 번 남았아요".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분 되었습니다.")

# customer = "아이언맨"
# index = 1
# while True:
#     print("{0}, 커피가 준비 되었습니다. 호출 {1} 회".format(customer, index))
#     index += 1

# customer = "토르"
# person = "Unknown"

# while person != customer:
#     print("{0}, 커피가 준비 되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요?")
#     if person == customer:
#         print("맛있게 드세요")
#     elif person != customer:
#         print("잠시만 더 기다려 주세요.")

# #continue와 break
# absent = [2, 5] #결석
# no_book = [7] #책을 깜빡했음
# for student in range(1, 11):
#     if student in absent:
#         continue
#     if student in no_book:
#         print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
#         break
#     print("{0}, 책을 읽어봐".format(student))

# #한줄로 끝내는 for문
# #출석 번호가 1 2 3 4, 앞에 100을 붙이기로 함 -> 101, 102, 103, 104
# student = [1,2,3,4,5]
# print(student)
# students = [i+100 for i in student]
# print(students)

# #학생 이름을 길이로 변환
# students = ["Iron man", "Thor", "I am groot"]
# students = [len(i) for i in students]
# print(students)

# #학생 이름을 대분자로 변환
# students = ["Iron man", "Thor", "I an groot"]
# students = [i.upper() for i in students]
# print(students)

'''
Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

조건1) 승객별 운행 소요 시간은 5분~50분 사이의 난수로 정해집니다.
조건2) 당신은 소요시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

(출력문 예제)
[0] 1번째 손님 (소요시간 : 15분)
[ ] 2번째 손님 (소요시간 : 50분)
[0] 3번째 손님 (소요시간 : 5분)
...
[ ] 50번째 손님 (소요시간 : 16분)

총 탑승 승객 : 2분
'''

# from random import *
# cnt = 0
# for i in range(1, 51):
#     time = randrange(5, 51)
#     if 5 <= time <= 15:
#         print("[0] {0}번째 손님 (소요시간: {1}분)".format(i, time))
#         cnt += 1
#     else:
#         print("[ ] {0}번째 손님 (소요 시간 : {1}분)".format(i, time))
# print("총 탑승 승객 : {0}분".format(cnt))

# #함수
# def open_account():
#     print("새로운 계좌가 생성되었습니다.")

# def deposit(balance, money):
#     print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance + money))
#     return balance + money

# def withdraw(balance, money):
#     if balance >= money:
#         print("{0}원이 출금이 완료되었습니다 잔액은 {1}원 입니다" .format(money, balance - money))
#         return balance - money
#     else:
#         print("출금이 완료되지 않았습니다. 잔액은 {0}원 입니다.".format(balance))
#         return balance

# def withdraw_night(balance, money):
#     commission = 100
#     return commission, balance - money - commission

# balance = 0
# balance = deposit(balance, 1000)
# # balance = withdraw(balance, 500)
# commission, balance = withdraw_night(balance, 500)
# print("수수료는 {0}원 이며, 잔액은 {1}원 입니다.".format(commission, balance))

# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))

# profile("유재석", 20, "python")
# profile("김태호", 25, "java")

#같은 학교 같은 학년 같은 반 같은 수업.

# def profile(name, age=17, main_lang="python"):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))

# profile("유재석")
# profile("김태호")

# def profile(name, age, main_lang):
#     print(name, age, main_lang)

# profile(name="유재석", age=20, main_lang="python")
# profile(main_lang="자바", age=25, name="김태호")

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name,age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)

# def profile(name, age, *language):
#     print("이름 : {0}\t나이 : {1}\t".format(name,age), end=" ")
#     for lang in language:
#         print(lang, end=" ")
#     print()

# profile("유재석", 20, "Python", "Jvaa", "C", "C++", "C#", "JavaScript")
# profile("김태호", 25, "Kotlin", "Swift", "", "", "")

# gun = 10

# def checkpoint(soldiers):
#     global gun
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun

# print("전체 총 : {0}".format(gun))
# # checkpoint(2)
# gun = checkpoint_ret(gun, 2)
# print("남은 총 : {0}".format(gun))

'''
Quiz) 표준 체중을 구하는 프로그램을 작성하시오

*표준 체중 : 각 개인의 키에 적당한 체중
(성별에 따른 공식)
 남자 : 키(m) x 키(m) x 22
 여자 : 키(m) x 키(m) x 21

조건1 : 표준 체중은 별도의 함수 내에서 계산
        * 함수명 : std_weight
        * 전달값 : 키(height), 성별(gender)
조건2 : 표준 체중은 소수점 둘쨰자리까지 표시

(출력 예제)
키 175cm 남자의 표준 체중은 67.38kg 입니다.

def std_weight(height, gender):
    if gender == "남자":
        result = height * height * 22
    else:
        result = height * height * 21
    return result

height = 179
gender = "남자"
result = round(std_weight(height / 100, gender), 2)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, result))
'''

# import sys
# print("Python", "Java", file=sys.stdout)
# print("Python", "Java", file=sys.stderr)

# #시험 성적
# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items():
#     # print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":")

# #은행 대기순번표
# #001, 002, 003, ...
# for num in range(1, 21):
#     print("대기번호 : " + str(num).zfill(3))

# answer = input("아무 값이나 입력하세요 : ")
# print("입력하신 값은 " +answer+ "입니다.")

#빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리공간을 확보
# print("{0: >10}".format(500))
#양수일 때는 +로 표기, 음수일 때는 -로 표시
# print("{0: >+10}".format(500))
# print("{0: >+10}".format(-500))
#왼쪽 정렬하고, 빈칸을 _로 채움
# print("{0:_<+10}".format(500))
# #3자리 마다 콤마를 찍어주기
# print("{0:,}".format(100000000000000))
# #3자리 마다 콤마를 찍어주고, +-부호도 붙이기
# print("{0:+,}".format(100000000000000))
# print("{0:+,}".format(-100000000000000))
# #3자리 마다 콤마를 찍어주고, 부호도 붙이고, 자릿수 확보하기
# #빈자리는 ^로 채워주기
# print("{0:^<+30,}".format(100000000000000))
#소수점 출력
# print("{0:f}".format(5/3))
# #소수점 특정 자리수 까지만 표시
# print("{0:.2f}".format(5/3))

#파일 입출력
# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="")
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines()
# for line in lines:
#     print(line, end="")
# score_file.close()

#pitkle
import pickle
# profile_file = open("profile.pickle", "wb")
# profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file)#profile에 있는 정보를 profile_file에 저장
# profile_file.close()

# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file)
# print(profile)
# profile_file.close()

#with문
# with open("profile.pickle", "rb") as profile_file:
    # print(pickle.load(profile_file))

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")

# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())

'''
Quiz) 당신의 회사에서는 매주 1회 장석해야 하는 보고서가 있습니다.
보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

- X 주차 주간보고 -
부서 : 
이름 : 
업무 요약 : 

1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.

조건 : 파일명은 "1주차.txt", "2주차.txt", ... 와 같이 만듭니다.

cnt = 1
for i in range(1, 3):
    filename = str(cnt) + "주차.txt"
    report_file = open(filename, "w", encoding="utf8")
    report_file.write("- {0}주차 주간보고 -".format(i))
    report_file.write("\n부서 : ")
    report_file.write("\n이름 : ")
    report_file.write("\n업무 요약 : ")
    cnt+=1
report_file.close()
'''

# #마린 : 공격 유닉, 군인, 총을 쏠 수 있음
# name = "마린"
# hp = 40
# damage = 5
# print("{} 유닛이 생성되었습니다.".format(name))
# print("체력은 {0}, 공격력은 {1}\n".format(hp, damage))

# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35
# print("{} 유닛이 생성되었습니다.".format(tank_name))
# print("체력은 {0}, 공격력은 {1}\n".format(tank_hp, tank_damage))

# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 : {2}]".format(name, location, damage))

# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)

# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성 되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

# wraith1 = Unit("레이스", 80, 5)
# print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# wraith2 = Unit("빼앗은 레이스", 80, 5)
# wraith2.clocking = True
# if wraith2.clocking == True:
#     print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))

# class AttactUnit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
        
#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0}, {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <=0 :
#             print("{0} : 파괴되었습니다.".format(self.name))

# firebat1 = AttactUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")
# firebat1.damaged(25)
# firebat1.damaged(25)

# 상속
# class Unit:
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp
       
# class AttactUnit(Unit):
#     def __init__(self, name, hp, damage):
#         Unit.__init__(self, name, hp)
#         self.damage = damage  

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0}, {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <=0 :
#             print("{0} : 파괴되었습니다.".format(self.name))

# #날 수 있는 기능을 가진 클래스
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

# #공중 공격 유닛 클래스
# class FlyableAttackUnit(AttactUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttactUnit.__init__(self, name, hp, damage)
#         Flyable.__init__(self, flying_speed)

#발키리(공중 공격유닛, 한번에 14마리 공격)
# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")

#오버로딩
# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed

#     def move(self, location):
#         print("[지상유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 : {2}]".format(self.name, location, self.speed))
       
# class AttactUnit(Unit):
#     def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage  

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0}, {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <=0 :
#             print("{0} : 파괴되었습니다.".format(self.name))

# #날 수 있는 기능을 가진 클래스
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

# #공중 공격 유닛 클래스
# class FlyableAttackUnit(AttactUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttactUnit.__init__(self, name, hp, 0, damage) # 지상스피드 = 0
#         Flyable.__init__(self, flying_speed)

#     def move(self, location):
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)

# #벌쳐 ( 기동성 좋음 )
# vulture = AttactUnit("벌처", 80, 10, 20)

# #배틀크루져
# battlecruiser = FlyableAttackUnit("배틀 크루져", 500, 25, 3)

# vulture.move("11시")
# battlecruiser.move("9시")

# from random import *

# #일반유닛
# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed
#         print("{0} 유닛이 생성되엇습니다.".format(name))

#     def move(self, location):
#         print("{0} : {1} 방향으로 이동합니다. [속도 : {2}]".format(self.name, location, self.speed))
    
#     def damaged(self, damage):
#         print("{0}, {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <=0 :
#             print("{0} : 파괴되었습니다.".format(self.name))
       
# #공격유닛
# class AttactUnit(Unit):
#     def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage  

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(self.name, location, self.damage))

# #마린
# class Marine(AttactUnit):
#     def __init__(self):
#         AttactUnit.__init__(self, "마린", 40, 1, 5)

#     # 스팀팩
#     def stimpack(self):
#         if self.hp > 10:
#             self.hp -=10
#             print("{0} : 스팀팩을 사용합니다. (HP10 감소)".format(self.name))
#         else:
#             print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))

# #탱크
# class Tank(AttactUnit):
#     #시즈모드
#     seize_developed = False # 시즈모드 개발여부

#     def __init__(self):
#         AttactUnit.__init__(self, "탱크", 150, 1, 35)
#         self.seize_mode = False

#     def set_seize_mode(self):
#         if Tank.seize_developed == False:
#             return

#         if self.seize_mode == False:
#             print("{0} : 시즈모드로 전환합니다.".format(self.name))
#             self.damage *= 2
#             self.seize_mode = True
#         else:
#             print("{0} : 시즈모드를 해제합니다.".format(self.name))
#             self.damage /= 2
#             self.seize_mode = False

# #날 수 있는 기능을 가진 클래스
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

# #공중 공격 유닛 클래스
# class FlyableAttackUnit(AttactUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttactUnit.__init__(self, name, hp, 0, damage) # 지상스피드 = 0
#         Flyable.__init__(self, flying_speed)

#     def move(self, location):
#         self.fly(self.name, location)

# #레이스
# class Wraith(FlyableAttackUnit):
#     def __init__(self):
#         FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
#         self.clocked = False

#     def clocking(self):
#         if self.clocked == True:
#             print("{0} : 클로킬 모드 해체합니다.".format(self.name))
#             self.clocked = False
#         else:
#             print("{0} : 클로킹 모드 설정합니다.".format(self.name))
#             self.clocked = True

# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")

# def game_over():
#     print("Player : gg")
#     print("[Player] 님이 게임에서 퇴장하셨습니다.")

# #실제 게임 진행
# game_start()

# m1 = Marine()
# m2 = Marine()
# m3 = Marine()

# t1 = Tank()
# t2 = Tank()

# w1 = Wraith()

# attack_units = []
# attack_units.append(m1)
# attack_units.append(m2)
# attack_units.append(m3)
# attack_units.append(t1)
# attack_units.append(t2)
# attack_units.append(w1)

# #전군 이동
# for unit in attack_units:
#     unit.move("1시")

# #탱크 시즈모드 개발
# Tank.seize_developed = True
# print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

# #공격 모드 준비 (마린: 스팀팩, 탱크: 시즈모드, 레이스: 클로킹)
# for unit in attack_units:
#     if isinstance(unit, Marine):
#         unit.stimpack()
#     elif isinstance(unit, Tank):
#         unit.set_seize_mode()
#     elif isinstance(unit, Wraith):
#         unit.clocking()

# #전군 공격
# for unit in attack_units:
#     unit.attack("1시")

# #전군 피해
# for unit in attack_units:
#     unit.damaged(randint(5,21))

# #게임 종료
# game_over()

# #건물
# #pass
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         pass

# #서플라이 디폿 (건물, 8인구 수 증가)
# supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")

# def game_over():
#     pass

# game_start()
# game_over()

# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         # Unit.__init__(self, name, hp, 0)
#         super().__init__(name, hp, 0)
#         self.location = location

'''
Quiz) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오.

(출력 예제)
총 3대의 매물이 잇습니다.
강남 아파트 매매 10억 2010년
마포 오피스텔 전세 5억 2007년
송파 빌라 월세 500/50 2000년
[코드]
'''
# class House:
#     #매물 초기화
#     def __init__(self, location, house_type, deal_type, price, completion_year):
#         self.location = location
#         self.house_type = house_type
#         self.deal_type = deal_type
#         self.price = price
#         self.completion_year = completion_year
    
#     #매물 정보 표시
#     def show_detail(self):
#         print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)

# houses = []
# house1 = House("강남", "아파트", "매매", "10억", "2010년")
# house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
# house3 = House("송파", "빌라", "월세", "500/50", "2000년")
# houses.append(house1)
# houses.append(house2)
# houses.append(house3)

# print("총 {0}대의 매물이 있습니다.".format(len(houses)))
# for house in houses:
#     house.show_detail()

# class Insert(House):
#     def __init__(self):
#         House.__init__("강남", "아파트", "매매", "10억", "2010년")

# try:
#     print("나누기 전용 계산기 입니다.")
#     num1 = int(input("첫번째 숫자를 입력하세요 : "))
#     num2 = int(input("두번째 숫자를 입력하세요 : "))
#     print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
# except ValueError:
#     print("에러! 잘못된 값을 입력하였습니다.")
# except ZeroDivisionError as err:
#     print(err)

# try:
#     print("나누기 전용 계산기 입니다.")
#     nums = []
#     nums.append(int(input("첫번째 숫자를 입력하세요 : ")))
#     nums.append(int(input("두번째 숫자를 입력하세요 : ")))
#     # nums.append(int(nums[0] / nums[1]))
#     print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
# except ValueError:
#     print("에러! 잘못된 값을 입력하였습니다.")
# except ZeroDivisionError as err:
#     print(err)
# except Exception as err:
#     print("알 수 없는 에러가 발생하였습니다.")
#     print(err)

# class BigNumberError(Exception):
#     def __init__(self, msg):
#         self.msg = msg

#     def __str__(self):
#         return self.msg

# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
#     print("{0}/{1}={2}".format(num1, num2, int(num1/num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
# except BigNumberError as err:
#     print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
#     print(err)
# finally:
#     print("계산기를 이용해 주셔서 감사합니다.")

'''
Quiz) 동네에 항상 대기 손님이 있는 맛있는 치킨집이 있습니다.
대기 손님의 치킨 요리 시간을 줄이고자 자동 주문 시스템을 제작하였습니다.
시스템 코드를 확인하고 적절한 예외처리 구문을 넣으시오.

조건1 : 1보다 작거나 숫자가 아닌 입력값이 들오올 떄는 ValueError로 처리
        출력 메시지 : "잘못된 값을 입력하였습니다."
조건2 : 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
        치킨 소진 시 사용자 정의 에러[SoldOutError]를 발생시키고 프로그램 종료
        출력 메시지 : "재고가 소진되어 더 이상 주문을 받지 않습니다."

'''

# class SoldOutError(Exception):
#     def __init__(self, msg):
#         self.mag = msg 
    
#     def __str__(self):
#         return self.mag

# chicken = 10
# waiting = 1
# while(True):
#     print("[남은 치킨 : {0}]".format(chicken))
#     try:    
#         order = int(input("치킨 몇 마리 주문하시겠습니까?"))
#         if order <= 0:
#             raise ValueError
#         if order > chicken:
#             print("재료가 부족합니다.")
#         else:
#             print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다".format(waiting, order))
#             waiting += 1
#             chicken -= order
#         if chicken == 0:
#             raise SoldOutError("재료가 소진되어 더 이상 주문을 받지 않습니다. 이용해주셔서 감사하빈다")
#     except SoldOutError as err:
#         print(err)
#     except ValueError as err:
#         print("잘못된 입력입니다. 숫자만 입력해 주세요.")
#     if chicken == 0:
#         break
    
#모듈
# import theater_module
# theater_module.price(3)
# theater_module.price_morning(4)
# theater_module.price_soldier(3)
# import theater_module as mv
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(3)
# from theater_module import *
# price(3)
# price_morning(4)
# price_soldier(3)
# from theater_module import price, price_morning
# price(5)
# price_morning(5)
# from theater_module import price_soldier as sol
# sol(3)

#패키지
# import travel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import *
# trip_to = thailand.ThailandPackage()
# trip_to.detail()
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# import inspect
# import random
# print(inspect.getfile(random))
# print(inspect.getfile(thailand))

# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())

##내장 함수
# language = input("무슨 언어를 좋아하세요?")
# print("{0}는 아주 좋은 언어입니다.".format(language))

#dir : 어떤 객체를 넘겨줬을때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# import random
# print(dir())
# import pickle
# print(dir(random))

# lst = [1, 2, 3]
# print(dir(lst))
# name = "Jim"
# print(dir(name))

#glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
# import glob
# print(glob.glob("*.py"))

#os : 운영체제에서 제공하는 기본 기능
# import os
# print(os.getcwd())

# folder = "sample_dir"
# if os.path.exists(folder):
#     print("이미 존재하는 폴더 입니다.")
#     os.rmdir(folder)
#     print(folder, "폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder)
#     print(folder, "폴더를 생성하였습니다.")
# print(os.listdir())

#time : 시간관련 함수
# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

# import datetime
# print("오늘 날짜는 ", datetime.date.today())
# today = datetime.date.today()
# td = datetime.timedelta(days=100)
# print("우리가 만난지 100일은", today + td)

'''
Quiz) 프로젝트 내에 나만의 시그니처를 남기는 모듈을 만드시오

조건 : 모듈 파일명은 byme.py로 작성

(모듈 사용 예제)
import byme
byme.sign()

(출력 예제)
이 프로그램은 나도코딩에 의해 만들어졌습니다.
유튜브 : 
이메일 : 
'''

# from pracmo.byme import Byme
# byme = Byme()
# byme.sign()
