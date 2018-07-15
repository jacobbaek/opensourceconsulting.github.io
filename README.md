# 오픈소스컨설팅 기술 블로그
## 기술을 나눕니다. 함께 성장합니다.

## 설명
기술 블로그를 GitHub Page로 이전 했습니다. </br>
GitHub Page를 선택한 이유는 HTML, CSS, Javascript를 자유롭게 수정하고 싶었습니다. <br/>
하지만 Infra, Middleware를 구성은 유지보수 이슈가 있었습니다. <br/>
GitHub Page는 이러한 고민을 해결해 주면서 `글 쓰기에` 집중 할 수 있습니다. <br/>
우리는 글을 작성하고 올리면 GitHub에서 웹 서비스를 해줍니다. <br/>
테마 적용에 약간의 코딩을 했지만 우리는 글을 작성하고 올리기만 하면 됩니다! <br/>
하지만 다른 블로그와 달리 `Git`을 조금 알아야 하구요. <br/>
`MarkDown`도 알아야 합니다. 어렵지 않습니다. <br/>
이 글을 읽고 해보시기 바랍니다.

## 환경 구성
우리는 GitHub에서 블로그 소스코드를 우리 컴퓨터에 복사 해야 합니다.<br/>
복사한 소스코드를 jekyll(네 맞습니다. 지킬앤하이드에 지킬입니다.)을 이용해서 작성한 글을 확인하고 빌드해서 GitHub에 추가할 것입니다.<br/>
Atom이라는 도구를 이용해서 글을 편집하고 GitHub에 추가해 보겠습니다.<br/>
Windows, Mac(Linux) 환경 구성 방법을 안내해 드리겠습니다. <br/>
설치만 했지 자세한건 몰라도 됩니다. 매우 쉽거든요! `:)`
### 설치 프로그램
  - Git (소스코드 관리)
  - Ruby (아름다운 언어)
  - jekyll (소스코드 빌드/서비스)
  - Atom (편집도구)

### Windows
 - Git 설치 https://git-scm.com/download/win <br/>
 - Ruby 설치  https://github.com/oneclick/rubyinstaller2/releases/download/rubyinstaller-2.5.1-2/rubyinstaller-devkit-2.5.1-2-x64.exe <br/>
 - `Start Command Prompt with Ruby` 실행
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

### macOS
Git 설치 [https://git-scm.com/download/mac] <br/>
Ruby Version 확인
```
Ruby -v
```

### 글 쓰기 (Windows & macOS)
에디터는 Atom으로 진행하지만 편하신걸로 아무거나 괜찮습니다!

 - Atom 설치 [ https://atom.io/ ]

자 이제 Step by step으로 진행 하겠습니다.

Step1. GitHub에서 블로그 소스코드 복사
 - `Windowns + R` = `cmd` 실행
 - git repository(저장소) Local(내 컴퓨터)에 복사
```
git clone git@github.com:OpenSourceConsulting/opensourceconsulting.github.io.git
```

  -



### Mac

## 작성 방법
### Branch 생성
### Create Pull Request
