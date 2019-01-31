---
layout: post
title: "ConfluencePage CSS꾸미기"
description: "Confluence CSS로 멋짐을 입혀서 가독성과 페이지를 이쁘게 꾸미는 방법을 소개합니다."  
author: it2seiyon
date: 2018-07-23
modified: 2018-07-23
tags: [Confluence, Atlassian, CSS]
category: Confluence, Atlassian
---  
# 오픈소스컨설팅 기술 블로그
## 기술을 나눕니다. 함께 성장합니다.

Confluence(이하 컨플루언스)는 간단한 방법으로 문서를 작성, 공유하는 도구입니다. 문서를 꾸미는데  
시간을 낭비하지 않고 고객이 원하는 서비스를 구현, 지원하는데 모든 걸 쏟아붓습니다.  

하지만, 우리가 어떤 민족입니까. `멋`, `간지`가 있어줘야 하지 않겠습니까. IT에서는 `멋`을 CSS라고 부르더군요. w3schools.com의 CSS는 소개는 이렇습니다.

> CSS stands for Cascading Style Sheets  
> CSS describes how HTML elements are to be displayed on screen, paper, or in other media  
> CSS saves a lot of work. It can control the layout of multiple web pages all at once  
> External stylesheets are stored in CSS files

`HTML`에 `멋`을 입힐 수 있다고합니다. 우리도 컨플루언스에 `멋`을 좀 내볼까요?  

## 사전조건
- 컨플루언스 관리자 (confluence-administrators)  
CSS로 `멋`을 내다보면 실수할 수도 있으니 운영시간 이외에 또는 테스트 환경에 우선 적용을 해보시기 바랍니다.


## h1 제목에 스타일 입히고 전체 폰트 키우기
![Confluence CSS]({{"/assets/images/h1_css.png"}})  
위 사진처럼 H1 제목에 강조하는 스타일을 적용하고 일반 텍스트 폰트 사이즈를 키워보겠습니다. 폰트가 작아서 좀 답답했거든요..  

 - `Admin menu` > `Look and feel` > `Stylesheet` 메뉴를 보시면  
 ![Confluence Menu 위치]({{"/assets/images/wiki_css_menu.png"}})[width=200]

 - Global CSS를 입력할 수 있습니다. `EDIT` 버튼으로 CSS를 입력합니다.  

 ![Confluence Global Stylesheet]({{"/assets/images/wiki_css.png"}})

 ```html
 /* main content는 page 글 부분입니다. */
#main-content h1{
  border-left: 5px solid black;
  padding-left: 5px;
}

/* 글씨 크기 키우기 */
#main-content p{
    font-size: 15px;
    padding-bottom: 5px; /* 글 간격 조정 */
}

/* 구두점 목록 글씨 크기 키우기 */
#main-content li {
  font-size: 15px;
  padding-bottom: 5px;
}
 ```

코드를 복사&붙여 넣기 후 바뀐 페이지를 확인할 수 있습니다.  
Edit할 때는 보이지 않지만 저장 후 보여요 :)  
간단한 방법으로 각자의 `멋`을 추가해보시는건 어떨까요?  

오픈소스컨설팅  
김세연  
atlassian@osci.kr  
