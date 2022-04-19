import re

p = re.compile("ca.e")

def print_match(m):
    if m:
        print("m.group() : ", m.group())
        print("m.string : ", m.string)
        print("m.start() : ", m.start())
        print("m.end() : ", m.end())
        print("m.span() : ", m.span())
    else:
        print("매칭되지 않음")

# m = p.match("careless") # match : 주어진 문자열의 처음부터 일치하는지 확인
# m = p.search("good care") # search : 주어진 문자열 중에 일치하는게 있는지 확인
# print_match(m)

lst =  p.findall("good care cafe") # findall : 일치하는 모든 것을 리스트 형태로 반환
print(lst)