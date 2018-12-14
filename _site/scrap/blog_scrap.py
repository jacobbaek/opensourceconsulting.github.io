import os
import time
import requests
from bs4 import BeautifulSoup

# 티스토리 블로그에는 총 71개의 글이 있다. 중간에 빠진 글도 있을 수 있다.
# 주소 http://blog.osci.kr/4  마지막에 게시글 번호가 있다.
# 증분으로 크롤링을 해보겠다.
# 이미지는 다운로드 받아서 마크다운으로 대체한다.

# 헤더 설정(설정하지 않으면 티스토리에서 막는다.)
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}

for post_number in range(1, 73):
    try:
        time.sleep(3)
        print(f'http://blog.osci.kr/{post_number}')
        url = f'http://blog.osci.kr/{post_number}'
        # get 방식으로 호출
        r = requests.get(url, headers=headers)
        # bs(BeautifulSoup)로 맵핑
        soup = BeautifulSoup(r.text, 'html.parser')

        # body 맵핑
        body = soup.find("div", {"class", "area_view"})

        #불필요한 html 제거
        for child in body.find('div', {'class': 'container_postbtn'}).children:
            child.decompose()
        body.find('iframe').decompose()

        post_title = soup.find('meta', {'name': 'title'})['content']
        post_date = soup.find('meta', {'property':'article:published_time'})['content']
        post_desc = soup.find('meta', {'name':'twitter:description'})['content']

        # 게시글 폴더 생성
        if not os.path.exists(f'../assets/images/{post_number}'):
            os.makedirs(f'../assets/images/{post_number}')

        # get image file name
        for img in body.find_all('img'):
            try:
                image_name = img['filename']
                image_src = img['src']
                # insert image markdown
                soup = BeautifulSoup('<div></div>', "html5lib")
                img_tag = soup.new_tag('img', src=f'/assets/images/{post_number}/{image_name}')
                img.insert_before(img_tag)
                print('downloading..', image_name, ', ', image_src)
                img_bin = requests.get(image_src, headers=headers)
                f = open(f'../assets/images/{post_number}/{image_name}', 'wb')
                f.write(img_bin.content)
                f.close()
                img.unwrap()
                time.sleep(1)
            except Exception as e:
                print(e)

        post_header = '---\n'
        post_header += 'layout: post\n'
        post_header += f'title: {post_title}\n'
        post_header += f'description: {post_desc}\n'
        post_header += 'author: it2seiyon\n'
        post_header += f'date: {post_date}\n'
        post_header += 'tags: [OpenSourceConsulting]\n'
        post_header += 'category: OpenSourceConsulting\n'
        post_header += '---\n'
        simple_date = post_date[0:10]
        post_file = open(f'./{simple_date}-tistory-{post_number}.md', 'w')
        post_file.write(post_header)
        post_file.write(body.prettify())
        post_file.close()

    except Exception as e:
        print(e)
