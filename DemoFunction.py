# DemoFunction.py 

#함수 정의 
def setValue(newValue):
    x = newValue
    print(x)

#호출 
print(setValue(5))

#튜플로 리턴 
def swap(x,y):
    return y,x 
#호출
print(swap(3,4))
#지역변수와 전역변수
x = 10 
def func(a):
    return a+x 
#호출
print(func(1))

def func2(a):
    x = 5 
    return a+x 
#호출
print(func2(1))

#기본값 셋팅
def times(a=10, b=20):
    return a*b 

print(times())
print(times(5))
print(times(5,6))

