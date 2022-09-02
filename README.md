# 제주도 병원 후기 모음 서비스

## 1. 목표와 기능

### 1.1 목표
- 지역 병원을 모아볼 수 있는 웹 서비스
- 해당 진료과목의 병원을 모아볼 수 있는 웹 서비스
- 영업을 하지 않는 병원은 노출이 되지 않아 혼선을 줄여주는 웹 서비스
- 해당 병원의 정보와 전반적인 후기를 모아보는 웹 서비스

### 1.2 기능
- 제주데이터허브 "[보건, 복지] 병,의원 정보" 사용(https://www.jejudatahub.net/data/view/data/859)
- 제주 지역과 진료과목에 따라 구분된 병원 목록 제공
- 병원의 만족도를 확인할 수 있는 별점 제공
- kakao map api 사용
- 로그인, 회원가입
- 후기 작성

## 2. 개발 환경 및 배포 URL
### 2.1 개발 환경
- Tools
    - Visual Studio Code, GitHub, Figma, Discord
- OS
    - Mac, Window10

### Back-End
- Web Framework
    - Django 3.2 (Python 3.6.8)
- 서비스 배포 환경
    - AWS Lightsail

### Front-End
- Web
    - HTML5, CSS, JavaScript
- API
    - Bootstrap5, Kakao Map

### 2.2 배포 URL
- http://jejuhospital.oreum.icu/

## 3. 프로젝트 구조와 개발 일정
```bash
  └─ hackathon
      └─ main
          └─ migrations
          └─ static
          └─ templates
          |  admin.py
          |  apps.py
          |  models.py
          |  tests.py
          |  views.py
      └─ media
      └─ myvenv(가상환경)
      └─ tutorialdjango
           |    asgi.py
           |    settings.py
           |    urls.py
           |    wsgi.py
      │  db.sqlite3
      |  manage.py 
```

### 3.1 개발 일정(WBS)

## 4. 역할 분담
- FE : 김승우
- FE : 정혜연
- BE : 허현주
- BE : 오민영

## 5. UI / BM
Main 화면
![image](https://user-images.githubusercontent.com/82134668/188096118-5845ec5a-375b-44ca-b6f2-b4e452d73b21.png)
HospitalDetail 화면
![image](https://user-images.githubusercontent.com/82134668/188096149-63d6867a-640b-418d-b607-69d9a214b6be.png)
Review 작성
![image](https://user-images.githubusercontent.com/82134668/188096199-b967ec17-9f32-4e59-a084-58e8da2663a6.png)
Review 완료
![image](https://user-images.githubusercontent.com/82134668/188096217-50820331-c1ad-49af-adec-124b8bc6163e.png)

## 6. 데이터베이스 모델링(ERD)
![ERwin](https://user-images.githubusercontent.com/94173023/188053009-61351f80-5786-4afb-b72d-7e21c1d2256d.jpg)

## 7. 메인 기능
- 반응형 웹페이지 : 창 사이즈에 따라 메뉴 구성 변화
    - header 메뉴바
    - content 진료과목 선택창
- 로그인, 회원가입 : 중복된 아이디, 비밀번호 입력 에러 등등 각 상태마다 alert 창 경고
- 제주데이터허브 공공데이터 : 병원리스트 제공
- 공공데이터의 최신버전으로 정렬하여 불러온 데이터 값의 중복 방지
- 병원의 디테일 정보 : 병원 이름, 주소, kakao map api를 사용한 주소 마킹, 후기 모음
- 후기 : 로그인한 사람에 한해서 사용가능, 제목, 내용, 별점이 다 작성되어야 등록 가능

## 8. 개발하면서 느낀점

- 오민영 : 급하게 잡힌 해커톤임에도 개개인의 시간을 들여 완성해나가는 모습이 인상깊었다. 배포를 하는 작업이다보니 사용자가 해당 웹페이지를 사용하는 과정에서 제한을 두기 위한 에러처리를 꼼꼼하게 하게 되었다.
- 정혜연 : 짧은 기간의 해커톤을 진행하면서 프로젝트를 이끌어가는 능력이 중요하다는 것을 느꼈고, 하나의 서비스를 완성하기 위해 서로 부족한 부분을 채워가며 협업이 진행된 것 같다. 정해진 시간 내에 깔끔하고 사용성 좋은 화면을 만들기 위해 CSS 중 일부 BootStrap을 적용하였다.
- 허현주 : 팀원들과 협업이 잘 이루어져서 정해진 기간내에 기획한 웹페이지를 제작 및 배포할 수 있었다. Front-End와 Back-End로 역할을 분담해서 진행해보는 좋은 경험이었다. api를 이용하여 기능을 구현하는 경험을 할 수 있었다.
- 김승우 : 처음하는 협업이 좋은 결과로 나올 수 있을것 같아 안심이 되었다. 같이 서비스를 만들면서 내가 어떤부분이 부족한지 알게되었다. 이번에는 FE만을 잡고 만들게 되었는데 더 좋은 서비스를 만들기 위해 BE에 대하여 공부를 해야겠다는 생각이 들었다.
