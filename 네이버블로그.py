import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

def crawl_naver_blog(search_keyword):
    wb = Workbook()
    ws = wb.active
    ws.append(["블로그명", "글 제목", "날짜"])
    
    for page in range(1, 101):  # 1페이지부터 100페이지까지
        url = f"https://search.naver.com/search.naver?where=view&sm=tab_jum&query={search_keyword}&start={page * 10 - 9}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            blog_list = soup.find_all('li', class_='bx _svp_item')

            for blog in blog_list:
                blog_name = blog.find('a', class_='sub_txt').text.strip()
                blog_title = blog.find('a', class_='api_txt_lines total_tit').text.strip()
                blog_date = blog.find('span', class_='sub_time sub_txt').text.strip()
                
                ws.append([blog_name, blog_title, blog_date])
        else:
            print("HTTP Error:", response.status_code)

    # 파일 저장
    wb.save("result.xlsx")
    print("result.xlsx 파일로 저장되었습니다.")

# 키워드 입력
search_keyword = input("검색할 키워드를 입력하세요: ")
crawl_naver_blog(search_keyword)
