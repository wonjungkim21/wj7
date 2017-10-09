
# coding: utf-8

# In[64]:

# Assignment Number..: 8
# Author.............: kim won jung
# File name..........: hw8c.py
# Written Date.......: 2017-07-14
# Program Description: 넘파이 모듈을 불러오고 어레이를 생성하는 방법을 익힌다. 넘파이 모듈을 활요해 간단한 통계량을 계산해본다.


import numpy
import unicodecsv #unicode 모듈을 불러온다.
car = open('car.csv', 'rb') #open 함수를 이용해 csv파일을 연다.
car_dic = unicodecsv.DictReader(car) #unicodecsv모듈의 DictReader()함수를 이용해 데이터를 불러오고 딕셔너리 형태로 변환한다.
car_l = list(car_dic) # 데이터를 리스트로 변환한다.

def parser_doors(a): #함수 parser_doors를 정의한다.

    if a['doors'] == '2': #doors의 인자값이 '2'이면 
        a['doors'] = 2     #2를 돌려준다.
    elif a['doors'] =='3': #doors의 인자값이 '3'이면
        a['doors'] = 3  # 3을 돌려준다.
    elif a['doors'] =='4': #doors의 인자값이 '4'이면
        a['doors'] = 4 # 를 돌려준다.
    elif a['doors'] =='5more': # doors의 인자값이 '5more'이면
        a['doors'] = 5 # 5를 돌려준다.
    return a #a를 리턴한다.

def parser_class(a):
    
    if a['class'] == 'unacc': #class의 인자값이 'unacc'이면
        a['class'] = 0 # 0을돌려준다.
    elif a['class'] == 'acc': #class의 인자값이 'acc'이면
        a['class'] = 1 #1을 돌려준다.
    elif a['class'] == 'good': #class의 인자값이 'good'이면
        a['class'] = 2 #2를 돌려준다.
    elif a['class'] == 'vgood': #class의 인자값이 'vgood'이면
        a['class'] = 3  # 3을 돌려준다.
    return a #a를 리턴한다.

k = [] #k라는 리스트를 생성한다.
for i in car_l: #car_l리스트를 for문을 이용해 반복하면
    a = parser_doors(i) #car_l의 첫번째 요소를 parser_doors함수를 이용해서 doors변수를 파싱한다.
    b =parser_class(a)  #parser_class함수를 이용해서 class변수를 파싱한다.
    k.append(b) #파싱한 결과를 k라는 리스트에 추가한다.
    

doors = [] #doors라는 리스트를 생성한다.
classes = [] #classes라는 리스트를 생성한다.

for i in k: #k라는 리스트를 for문을 이용해 반복하면
    a = (i['doors']) #a라는 변수에 doors의 값을 할당한다.
    doors.append(a) #그리고 a를 doors라는 리스트의 요소로 추가한다.
    c = (i['class']) #c라는 변수에 class의 값을 할당한다.
    classes.append(c) #그리고 c를 classes라는 리스트의 요소로 추가한다.
print(doors[:5]) #doors리스트의 처음 5개값을 출력한다.

doors_np = numpy.array(doors) #numpy모듈을 활용해 door리스트를 doors_np에 할당한다.
print(numpy.ndarray.mean(doors_np)) #door_np의 평균을 계산하고 출력한다.
print(numpy.ndarray.std(doors_np))  #door_np의 표준편차를 계산하고 출력한다.

classes_np = numpy.array(classes) #numpy모듈을 활용해 classes리스트를 classes_np에 할당한다.
print(numpy.corrcoef(doors_np, classes_np)) #doors_np와 classes_np간의 표본상관계수를 계산하고 출력해본다.


# In[ ]:



