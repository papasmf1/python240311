# web1.py 
#웹크롤링을 위한 선언 
from bs4 import BeautifulSoup

#페이지를 로딩
page = open("test01.html", "rt", encoding="utf-8").read() 
#검색이 용이한 객체 생성
soup = BeautifulSoup(page, "html.parser")
#print(soup.prettify())
#문서의 <p>전체 검색 
#print(soup.find_all("p"))
#print(soup.find_all("a"))
#하나의 <p>태그만 검색
#print(soup.find("p"))
#조건이 있는 경우:<p class='outer-text'>컨텐츠</p>
#class키워드와 충돌이 발생: class_
#print(soup.find_all("p", class_="outer-text"))
#attrs를 사용 
#print(soup.find_all("p", attrs={"class":"outer-text"}))

#태그의 내부 문자열만 가져오기: .text속성
for tag in soup.find_all("p"):
    title = tag.text.strip() 
    title = title.replace("\n", "")
    print(title)


