import json
file = []
for i in range(361, 473):
    file.append(json.load(open(f'../../013.피트니스자세_sample/라벨링데이터/D08-1-{i}.json', 'rt', encoding='utf8')))

# print(len(file))

# 0 ~ 15 : 오버헤드프레스
# type_info.conditions.condition[0] : 척추의 중립
# type_info.conditions.condition[1] : 전완 지면과 수직
# type_info.conditions.condition[2] : 견갑대 고정
# type_info.conditions.condition[3] : 무릎 반동 없음

# 16 ~ 47 : 레터럴 레이즈
# type_info.conditions.condition[0] : 무릎 반동 없음
# type_info.conditions.condition[1] : 어깨 으쓱 없음
# type_info.conditions.condition[2] : 상완과 전완의 각도 고정
# type_info.conditions.condition[3] : 손목의 각도 고정
# type_info.conditions.condition[4] : 상체 반동 없음

# 48 ~ 79 : 바벨 컬
# type_info.conditions.condition[0] : 팔꿈치 위치 고정
# type_info.conditions.condition[1] : 손목의 중립
# type_info.conditions.condition[2] : 척추의 중립
# type_info.conditions.condition[3] : 이완 시 팔 긴장 유지
# type_info.conditions.condition[4] : 수축 시 어깨 으쓱 없음

# 80 ~ 111 : 덤벨컬
# type_info.conditions.condition[0] : 팔꿈치 위치 고정
# type_info.conditions.condition[1] : 손목의 중립
# type_info.conditions.condition[2] : 척추의 중립
# type_info.conditions.condition[3] : 이완시 팔 긴장 유지
# type_info.conditions.condition[4] : 수축 시 어깨 으쓱 없음

# for idx, i in enumerate(range(len(file))):
#     print(idx, file[i]['type_info']['conditions'])

    
# print(file[1]['type_info'])
print(file[8]['frames'])