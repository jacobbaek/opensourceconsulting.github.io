# 오픈소스컨설팅 기술 블로그
## 기술을 나눕니다. 함께 성장합니다.

## 설명
기술 블로그를 GitHub Page로 이전 했습니다.  
GitHub Page를 선택한 이유는 HTML, CSS, Javascript를 자유롭게 수정하고 싶었습니다.   
하지만 Infra, Middleware를 구성은 유지보수 이슈가 있었습니다.  
GitHub Page는 이러한 고민을 해결해 주면서 `글 쓰기에` 집중 할 수 있습니다.  
우리는 글을 작성하고 올리면 GitHub에서 웹 서비스를 해줍니다.  
테마 적용에 약간의 코딩을 했지만 우리는 글을 작성하고 올리기만 하면 됩니다!  
하지만 다른 블로그와 달리 `Git`을 조금 알아야 하구요.  
`MarkDown`도 알아야 합니다. 어렵지 않습니다.  
이 글을 읽고 해보시기 바랍니다.

## GitHub 회원가입
아직 가입 안하셨습니다. 이번 기회에 가입해 보세요  
오픈소스컨설팅 기술 블로그로 감을 익히시고 `개인 블로그` 운영도 해보세요 :)

## 환경 구성
우리는 GitHub에서 블로그 소스코드를 우리 컴퓨터에 복사 해야 합니다.  
복사한 소스코드를 jekyll(네 맞습니다. 지킬앤하이드에 지킬입니다.)을 이용해서 작성한 글을 확인하고 빌드해서 GitHub에 추가할 것입니다.  
Atom이라는 도구를 이용해서 글을 편집하고 GitHub에 추가해 보겠습니다.  
Windows, Mac(Linux) 환경 구성 방법을 안내해 드리겠습니다.  
설치만 했지 자세한건 몰라도 됩니다. 매우 쉽거든요! `:)`

### 설치 프로그램
  - Git (소스코드 관리)
  - Ruby (아름다운 언어)
  - jekyll (소스코드 빌드/서비스)
  - Atom (편집도구)

### Windows
 - Git 설치 https://git-scm.com/download/win  
 - Ruby 설치  https://github.com/oneclick/rubyinstaller2/releases/download/rubyinstaller-2.5.1-2/rubyinstaller-devkit-2.5.1-2-x64.exe   
 - `Start Command Prompt with Ruby` 실행
 - utf8 설정
```
C:\Users\sy\work>chcp 65001
```
 - GitHub 블로그 Clone (폴더가 생성됩니다. 작업 위치 선정 필요합니다.)
```
C:\Users\sy\work>git clone git@github.com:OpenSourceConsulting/opensourceconsulting.github.io.git
```
 - jekyll 설치
```
C:\Users\sy\work\opensourceconsulting.github.io>gem install bundler jekyll
Fetching: bundler-1.16.2.gem (100%)
Successfully installed bundler-1.16.2
Parsing documentation for bundler-1.16.2
Installing ri documentation for bundler-1.16.2
Done installing documentation for bundler after 11 seconds
Fetching: public_suffix-3.0.2.gem (100%)
Successfully installed public_suffix-3.0.2
Fetching: addressable-2.5.2.gem (100%)
Successfully installed addressable-2.5.2
Fetching: colorator-1.1.0.gem (100%)
Successfully installed colorator-1.1.0
Fetching: http_parser.rb-0.6.0.gem (100%)
MSYS2 could not be found. Please run 'ridk install'
or download and install MSYS2 manually from https://msys2.github.io/
```
 - 블로그 bundle install
```
C:\Users\sy\work\opensourceconsulting.github.io>bundle install
```
 - 내 컴퓨터(local)에 jekyll build 및 서버 실행
 > jekyll build는 웹 사이트에 보여지는 코드를 생성한다.  
 > 우리는 build된 코드를 배포해야 한다.

 ```
  C:\Users\sy\work\opensourceconsulting.github.io>bundle exec jekyll serve

  Configuration file: C:/Users/sy/work/opensourceconsulting.github.io/_config.yml
     GitHub Metadata: No GitHub API authentication could be found. Some fields may be missing or have incorrect data.
              Source: C:/Users/sy/work/opensourceconsulting.github.io
         Destination: C:/Users/sy/work/opensourceconsulting.github.io/_site
   Incremental build: disabled. Enable with --incremental
        Generating...
                      done in 8.31 seconds.
   Auto-regeneration: enabled for 'C:/Users/sy/work/opensourceconsulting.github.io'
      Server address: http://127.0.0.1:4000/
    Server running... press ctrl-c to stop.
  ```

### macOS
 - Git 설치 [https://git-scm.com/download/mac]  
 - Ruby Version 확인
```
> Ruby -v
ruby 2.3.3p222 (2016-11-21 revision 56859) [universal.x86_64-darwin17]
```
 - Jekyll 설치
```
> gem install bundler jekyll
```
 - GitHub 저장소 복사
 ```
 > git clone git@github.com:OpenSourceConsulting/opensourceconsulting.github.io.git
 ```

 - bundle install
 ```
 opensourceconsulting.github.io>bundle install
 ```
 - 내 컴퓨터(local)에 jekyll build 및 서버 실행
 ```
 opensourceconsulting.github.io>bundle exec jekyll serve
 ```


### 글 쓰기 (Windows & macOS)
에디터는 Atom으로 진행하지만 편하신걸로 아무거나 괜찮습니다!  
`Jira Issue key`로 `브랜치를 생성`하여 글을 작성하고 `Pull Request`로 작성한 글을 승인 받고 웹에 퍼블리싱하는 과정을 설명하겠습니다.                   
 - Jira Issue 생성  
 https://jira.osci.kr/secure/RapidBoard.jspa?rapidView=98&projectKey=TB
  이슈를 생성해 주세요.

 - Git Branch 생성  
 블로그 위치에서 `git checkout -b <issue key>` 이슈키로 브랜치를 생성합니다.
 opensourceconsulting.github.io>git checkout TB-5

 - Atom 설치 [ https://atom.io/ ]  
 File > Open > opensourceconsulting.github.io `open`  

 - 글 생성  
 `_posts` 폴더에 yyyy-mm-dd-title.md 파일 생성  
 다른 post의 header를 참고로 page 정보 기입  

 - 마크다운  
 ```  
 # This is a H1  
 ## This is a H2  
 ### This is a H3  
 #### This is a H4  
 ##### This is a H5  
 ###### This is a H6  

 Enter는 스페이스 2개  
 ```
 code block  
4개의 스페이스 또는 tab이 시작되고 끝나는 부분까지 코드로 인식
       ``` This is a normal paragraph: This is a code block. end code block. ```

       마크다운 링크 참고 https://gist.github.com/ihoneymon/652be052a0727ad59601
 - 이미지 첨부  
 ```
 /assets/images/ 경로에 이미지 파일 삽입
 ![이미지 설명]({{ "/assets/images/fileName.png" | absolute_url }})
 ```

- 글 작성 후 jekyll로 로컬에서 확인  
      opensourceconsulting.github.io>bundle exec jekyll serve
http://127.0.0.1:4000/ post 확인

- git status  
`opensourceconsulting.github.io>git status` 수정한 파일을 확인합니다.

- git add  
`opensourceconsulting.github.io>git add .`수정된 파일 모두 Staging에 추가합니다. add 띄고 점이 있어요.

- git commit  
`opensourceconsulting.github.io>git commit -m "Update readme"` 수정된 파일 저장소에 저장합니다. `-m`은 commit message입니다. 동사로 시작하며 첫 문자만 대문자로 해주면 좋아요.(나중에 보기에 이뻐요...)

- git push  
`opensourceconsulting.github.io>git push` 원격 저장소에 생성한 브랜치를 업로드 합니다.

- Create Pull Request  
GitHub에서 생성한 브랜치를 Master에 Merge를 하는 행위입니다.  
GitHub URL [https://github.com/OpenSourceConsulting/opensourceconsulting.github.io]  
![Branch 메뉴]({{"/assets/images/branch_1.png | absolute_url"}})  
![New Pull Request]({{"/assets/images/branch_2.png | absolute_url"}})  
![Open Pull Request]({{"/assets/images/branch_3.png | absolute_url"}})  
Title에는 Jira 이슈키와 간단한 제목을 적어줍니다.  
Description은 선택사항 입니다.  
`Create Pull Request` 버튼으로 Pull Request를 생성합니다.

## 마무리
`GitHub` 가입을 시작으로 `Git`, `Ruby`, `Jekyll`, `Atom`을 설치했습니다.  
글을 작성하기 위해서 내 컴퓨터에 GitHub 원격 저장소를 `git clone` 명령어로 저장 했습니다.
Atom 에디터로 Post를 작성하기 위해서 Markdown을 습득했습니다.  
글 작성이 완료되고 `git add`로 Staging 환경에 저장했습니다. Staging 환경에는 자주 저장해도 좋습니다.  
모두 마무리가 됐다면 `git commit`으로 저장소에 저장하고 `git push`로 원격 저장소에 업로드까지 했습니다.
마지막으로 `Create Pull Request`로 Master 브랜치에 Merge까지 했습니다.
기술 블로그 글 작성을 통해서 `Git`의 기본 기능과 `Markdown`을 익혀보시면 좋을 것 같습니다.
