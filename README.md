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
<iframe width="600" height="336" src="https://www.erdcloud.com/p/F3osxKGyShsE2eWCb" frameborder="0" allowfullscreen></iframe>

## 7. 메인 기능

## 8. 개발하면서 느낀점