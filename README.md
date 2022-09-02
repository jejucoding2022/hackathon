# 제주도 병원 후기 모음 서비스

## 1. 목표와 기능

### 1.1 목표
- 지역 병원을 모아볼 수 있는 웹 서비스
- 해당 병원의 진료과목을 모아볼 수 있는 웹 서비스
- 영업을 하지 않는 병원은 노출이 되지 않아 혼선을 줄여주는 웹 서비스
- 해당 병원의 정보와 전반적인 후기를 모아보는 웹 서비스

### 1.2 기능
- 제주데이터허브 "[보건, 복지] 병,의원 정보" 사용(https://www.jejudatahub.net/data/view/data/859)
- kakao map api 사용
- 로그인, 회원가입
- 후기 작성

## 2. 개발 환경 및 배포 URL
### 2.1 개발 환경
- Web Framework
    - Django 3.1(Python 3.10)
- 서비스 배포 환경
    - vultr docker container

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

## 6. 데이터베이스 모델링(ERD)
![ERwin](https://user-images.githubusercontent.com/94173023/188053009-61351f80-5786-4afb-b72d-7e21c1d2256d.jpg)

## 7. 메인 기능
- 반응형 웹페이지 : 창 사이즈에 따라 메뉴 구성 변화
    - header 메뉴바
    - content 진료과목 선택창
​- 로그인, 회원가입 : 중복된 아이디, 비밀번호 입력 에러 등등 각 상태마다 alert 창 경고
- 제주데이터허브 공공데이터 : 병원리스트 제공
- 공공데이터의 최신버전으로 정렬하여 불러온 데이터 값의 중복 방지
- 병원의 디테일 정보 : 병원 이름, 주소, kakao map api를 사용한 주소 마킹, 후기 모음
- 후기 : 로그인한 사람에 한해서 사용가능, 제목,내용,별점이 다 작성되어야 등록 가능

## 8. 개발하면서 느낀점

- 오민영 : 급하게 잡힌 해커톤임에도 개개인의 시간을 들여 완성해나가는 모습이 인상깊었다. 배포를 하는 작업이다보니 사용자가 해당 웹페이지를 사용하는 과정에서 제한을 두기 위한 에러처리를 꼼꼼하게 하게 되었다.