# Assignment Number..: 6
# Author.............: kim won jung
# File name..........: hw6c.py
# Written Date.......: 2017-07-11
# Program Description: 패키지와 모듈을 불러오는법을 익히고, csv파일을 불러와 읽는 방법을 읽힌다.

from bs4 import BeautifulSoup #bs4패키지에서 BeautifulSoup를 불러온다.
from urllib.request import urlopen #urllib.request패키지에서 urlopen을 불러온다.

url = 'https://en.wikipedia.org/wiki/List_of_Presidents_of_the_United_States' #url이라는 변수에 'https://en.wikipedia.org/wiki/List_of_Presidents_of_the_United_States'에 할당한다.
web = urlopen(url) # web변수에 저장한다.

source = BeautifulSoup(web , 'html.parser') #BeautilfulSoup함수로 url을 파싱한다.

table = source.findAll(attrs = {'class' : 'wikitable'}) #wikitable이라는 클래스의 모든것을 table변수에  findAll()함수를 이용해서 저장한다.

a = table[0].findAll('big') # 리스트 table의 첫번째 인자의 big이라는 html태그를 가진 하위항목을 a라는 변수에 findAll함수를 이용해서 저장한다.

for i in a[:10]:  # for문을 이용해서 a라는 리스트의 10번째 까지 반복한다.
	print(i.get_text()) #get.text()함수를 이용하여 text부분만을 출력 한다.

