# Assignment Number..: 7
# Author.............: kim won jung
# File name..........: hw7c.py
# Written Date.......: 2017-07-14
# Program Description: 콤마로 분리된 데이터셋을 불러오고 파싱하는 방법을 익힌다. 데이터분석을 위해 데이터를 전처리하는 방법을 익힌다. 범주형 데이터를 인코딩하는 방법을 익힌다.

import unicodecsv #unicode 모듈을 불러온다.

car = open('car.csv', 'rb') #open 함수를 이용해 csv파일을 연다.
car_dic = unicodecsv.DictReader(car) #unicodecsv모듈의 DictReader()함수를 이용해 데이터를 불러오고 딕셔너리 형태로 변환한다.
car_l = list(car_dic) # 데이터를 리스트로 변환한다.
print(car_l[0]) #리스트에서 첫번째 요소를 출력한다.


# In[58]:

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

print(k[0]) #k의 첫번째 요소를 출력한다.
