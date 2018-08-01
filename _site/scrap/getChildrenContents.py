# -*- coding:utf-8 -*-
import json
import time, os
import requests
import urllib.parse
from bs4 import BeautifulSoup, NavigableString
from env import env

base_url = env['wiki_base_url']
content_id = env['wiki_content_id']
user = env['wiki_id']
password = env['wiki_password']
req_url = f'{base_url}/rest/api/content/{content_id}/child/page'

# get children
r = requests.get(req_url,
    auth=(user, password),
    headers=({'Content-Type': 'application/json'}))

children = r.json()
children_url = list()

for child in children['results']:
    children_url.append(child['id'])


# get child contents
for body in children_url:
    print('content id', body)
    r = requests.get(f'{base_url}/rest/api/content/{body}?expand=body.view',
        auth=(user, password),
        headers=({'Content-Type': 'application/json'}))
    data = r.json()
    body_html = data['body']['view']['value']
    body_soup = BeautifulSoup(body_html, "html.parser")

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
    cnt=0
    for img in body_soup.find_all('img'):
        try:
            img_src = urllib.parse.unquote(img['src'])
            img_tag = '![]({{' + f'"/assets/images/{body}/{cnt}"' + '}})'
            img.insert_before(img_tag)
            img_bin = requests.get(f'{base_url}{img_src}', auth=(user, password))
            print('downloading..', f'{base_url}{img_src}')
            f = open(f'../assets/images/{body}/{cnt}', 'wb')
            f.write(img_bin.content)
            f.close()
            img.unwrap()
            cnt+=1
            time.sleep(1)
        except Exception as e:
            print(e)

    # create post
    post_header = '---\n'
    post_header += 'layout: post\n'
    post_header += f'title: {title}\n'
    post_header += f'description: " " \n'
    post_header += f'author: {created_by}\n'
    post_header += f'date: {created_date}\n'
    post_header += 'tags: []\n'
    post_header += 'category: \n'
    post_header += '---\n'

    #remove tags
    tags = ['span', 'h1', 'h2', 'h3', 'h4', 'br', 'strong']
    for tag in tags:
        for r_tag in body_soup.find_all(tag):
            if r_tag.name == 'h1':
                r_tag.insert_before('# ')
            if r_tag.name == 'h2':
                r_tag.insert_before('## ')
            if r_tag.name == 'h3':
                r_tag.insert_before('### ')
            if r_tag.name == 'h4':
                r_tag.insert_before('#### ')
            r_tag.replaceWithChildren()

    #remove p tag
    post = body_soup.prettify()
    post = post.replace('\n', '')
    post = post.replace('<p>', '')
    post = post.replace('</p>', '  \n')

    post_file = open(f'../_posts/{created_date}-{body}.md', 'w')
    post_file.write(post_header)
    post_file.write(post)
    post_file.close()
