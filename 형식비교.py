# List: 변경 가능한(mutable) 시퀀스 자료형
my_list = [1, 2, 3, 4, 5]

# Tuple: 변경 불가능한(immutable) 시퀀스 자료형
my_tuple = (1, 2, 3, 4, 5)

# Dict: 키-값 쌍으로 이루어진 해시 테이블 자료형
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# List 요소 추가 및 삭제
my_list.append(6)
my_list.remove(3)

# Tuple은 변경이 불가능하므로 수정이 불가능

# Dict 요소 추가 및 삭제
my_dict['f'] = 6
del my_dict['c']

# 출력
print("List:", my_list)
print("Tuple:", my_tuple)
print("Dict:", my_dict)