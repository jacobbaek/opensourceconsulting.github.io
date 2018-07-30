# -*- coding:utf-8 -*-
import requests, json
from bs4 import BeautifulSoup

def jsonPrint(r):
    print ('{} {}\n'.format(json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': ')), r))

#get children
r = requests.get('http://wiki.osci.kr/rest/api/content/44204213/child/page', \
auth=(,), \
headers=({'Content-Type':'application/json'}))

children = r.json()
children_url = list()

for child in children['results']:
    children_url.append(child['id'])


#get child contents
for body in children_url:
    print('content id', body)
    r = requests.get(f'http://wiki.osci.kr/rest/api/content/{body}?expand=body.view', \
    auth=(,), \
    headers=({'Content-Type':'application/json'}))
    data = r.json()
    body = data['body']['view']['value']
    soup = BeautifulSoup(body, "html.parser")
    ##for img in soup.find_all('img'):
            # try:
            #     image_name = img['filename']
            #     image_src = img['src']
            #     # insert image markdown
            #     soup = BeautifulSoup('<div></div>', "html5lib")
            #     img_tag = soup.new_tag('img', src=f'/assets/images/{post_number}/{image_name}')
            #     img.insert_before(img_tag)
            #     print('downloading..', image_name, ', ', image_src)
            #     img_bin = requests.get(image_src, headers=headers)
            #     f = open(f'../assets/images/{post_number}/{image_name}', 'wb')
            #     f.write(img_bin.content)
            #     f.close()
            #     img.unwrap()
            #     time.sleep(1)
            # except Exception as e:
            #     print(e)