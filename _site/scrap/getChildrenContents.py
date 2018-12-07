# -*- coding:utf-8 -*-
import time
import os
import requests
import urllib.parse
from bs4 import BeautifulSoup
import env

base_url = env.env['wiki_base_url']
content_id = env.env['wiki_content_id']
user = env.env['wiki_id']
password = env.env['wiki_password']
req_url = f'{base_url}/rest/api/content/{content_id}/child/page'

# get children
r = requests.get(req_url, auth=(user, password), headers=({'Content-Type': 'application/json'}))

children = r.json()
children_url = list()

for child in children['results']:
    children_url.append(child['id'])

# get child contents
for body in children_url:
    r = requests.get(f'{base_url}/rest/api/content/{body}?expand=body.view',
                     auth=(user, password),
                     headers=({'Content-Type': 'application/json'}))
    data = r.json()
    body_html = data['body']['view']['value']
    body_soup = BeautifulSoup(body_html, "html.parser")

    # get label
    r = requests.get(f'{base_url}/rest/api/content/{body}/label',
                     auth=(user, password),
                     headers=({'Content-Type': 'application/json'}))
    label_data = r.json()

    is_published = False
    for label in label_data['results']:
        if label['name'] == 'published':
            is_published = True
            print(':+:+:+:', data['title'], ' published ', ':+:+:+:')
            break

    if is_published:
        continue

    print(':+:+:+:', data['title'], ' Start ', ':+:+:+:')
    print(body_soup.prettify())

    # get history
    h = requests.get(f'{base_url}/rest/api/content/{body}?expand=history',
                     auth=(user, password),
                     headers=({'Content-Type': 'application/json'}))
    his_data = h.json()

    created_by = his_data['history']['createdBy']['username']
    display_name = his_data['history']['createdBy']['displayName']
    created_date = his_data['history']['createdDate'][0:10]
    title = data['title']

    # download images
    if not os.path.exists(f'../assets/images/{body}'):
        os.makedirs(f'../assets/images/{body}')
    cnt = 0
    for img in body_soup.find_all('img'):
        try:
            img_src = urllib.parse.unquote(img['src'])
            img_tag = BeautifulSoup(f'<img src="/assets/images/{body}/{cnt}">', "html.parser")
            img.insert_before(img_tag)
            img_bin = requests.get(f'{base_url}{img_src}', auth=(user, password))
            print('downloading..',len(img_bin.content),' ', f'{img_src}')
            f = open(f'../assets/images/{body}/{cnt}', 'wb')
            f.write(img_bin.content)
            f.close()
            img.unwrap()
            cnt += 1
            time.sleep(1)
        except Exception as e:
            print(e)

    print('\n\n\n', body_soup.prettify())
    # create post
    post_header = '---\n'
    post_header += 'layout: post\n'
    post_header += f'title: "{title}"\n'
    post_header += f'description: " " \n'
    post_header += f'author: {created_by}\n'
    post_header += f'date: {created_date}\n'
    post_header += 'tags: []\n'
    post_header += 'category: \n'
    post_header += 'image: \n'
    post_header += '---\n'

    #
    # for r_tag in body_soup.find_all('p'):
    #     try:
    #         if len(r_tag.text) == 0:
    #             r_tag.extract()
    #     except Exception as e:
    #         print(e)

    post_file = open(f'../_posts/{created_date}-{body}.html', 'w')
    post_file.write(post_header)
    post_file.write(body_soup.prettify())
    post_file.close()
    print('\n\n')
