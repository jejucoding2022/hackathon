import json
import requests

from django.db.models import Avg
from django.shortcuts import render, redirect
from .models import User
from django.http import Http404

from main.models import Review

your_appkey = '1o1o1b_11_tppcjrcej7tr4cj14rc11o'
status = '영업/정상'
bizSmallType='병원'

locations = [
    '한경면', 
    '한림읍',
    '애월읍', 
    '제주시', 
    '조천읍', 
    '구좌읍',
    '대정읍',
    '안덕면',
    '서귀포시',
    '남원읍',
    '표선면',
    '성산읍',
    '우도면',
]

subjects = [
    ('내과'),
    ('정신건강의학과'),
    ('외과'),
    ('마취통증의학과'),
    ('산부인과'),
    ('소아청소년과'),
    ('이비인후과'),
    ('영상의학과'),
    ('병리과'),
    ('가정의학과'),
    ('치과')
]

# api 반복 호출을 방지하는 global 변수
url_data = ""

def jsondecode():
    global url_data
    # 전역변수에 데이터가 있으면 그 데이터 사용
    if url_data != "":
        return url_data
    else:
        try:
            # 병원api
            url = f'https://open.jejudatahub.net/api/proxy/tbb1D1a1559at91ababaata1abtba58a/{your_appkey}?openStatus={status}&bizSmallType={bizSmallType}&limit=100'
            response = requests.get(url)
            data = response.json()
            
            # api로 불러오는 데이터는 전역변수에 저장해서 api 반복호출을 방지한다.
            url_data = data.copy()
            return url_data
        # api 불러오지 못해 JSONDecode Error 발생시 안내
        except json.JSONDecodeError as e:
            raise Http404('페이지를 찾을 수 없습니다.새로고침을 시도해보십시오.') 



def index(request):  
    context = {
        'locations':locations
    }

    return render(request, 'main/index.html', context)


# 로그인
def login(request):
    if request.method == "GET":
        return render(request, 'main/login.html')
    elif request.method == 'POST':
        context = {}

        user_id = request.POST.get('user_id')
        password = request.POST.get('password')

        # 로그인 체크
        rs = User.objects.filter(user_id=user_id, password=password).first()
        print(user_id + '/' + password)
        print(rs)

        if rs is not None:
            request.session['user_id'] = user_id
            request.session['name'] = rs.name

            context={
                'user_id': user_id,
                'name': rs.name,
                'message': rs.name + "님 환영합니다.", # 수정 (hyunju_20220831)
                'locations':locations
            }
            return render(request, 'main/index.html', context)
        else:
            context['message'] = "id와 pw를 확인 후 다시 시도해주세요."
            return render(request, 'main/login.html', context)

    return render(request, 'main/login.html')


# 로그아웃
def logout(request):
    request.session.flush()
    #context['message'] = "로그아웃 되었습니다."
    # return redirect('/', context)
    context = {
        #'message': "로그아웃 되었습니다.", # 수정 (hyunju_20220902)
        'locations' : locations # 추가 (hyunju_20220831)
    }
    next_url = request.GET.get('next')
    return redirect(next_url)
    #return redirect('index') # 수정 (hyunju_20220831)
    #return render(request, '', context) # 수정 (hyunju_20220902)


# 회원가입
def user_regist(request):
    if request.method == "GET":
        return render(request, 'main/user_regist.html')
    elif request.method == 'POST':
        user_id=request.POST['user_id']
        password=request.POST['password']
        name=request.POST['name']
        phone=request.POST['phone']
        birth=request.POST['birth']
        user_image=request.FILES.get('user_image')

        # birth YYYY-MM-DD 형식 확인
        if not '-' in birth:
            context = {
                'message': "형식을 지켜주세요!",
                'locations': locations,
            }
            return render(request, 'main/user_regist.html', context)
        
        # 회원가입 중복체크
        rs = User.objects.filter(user_id=user_id)
        if rs.exists():
            context['message'] = user_id + "가 중복됩니다."
            return render(request, 'main/user_regist.html', context)
        else:
            User.objects.create(
                user_id=user_id, password=password,  name=name, phone=phone, birth=birth, user_image=user_image)
            #context['message'] = name + "님 회원가입 되었습니다."
            context = {
                'message': name + "님 회원가입 되었습니다.",
                'locations': locations,
            }
            return render(request, 'main/index.html', context)



def hospitallist(request):
    selected_locations = request.GET.getlist('locations')
    request.session['selected_locations'] = selected_locations

    data = jsondecode()

    context={
        'selected_locations': selected_locations,
        'data':data,
        'subjects':subjects
    }
    return render(request, 'main/hospitallist.html', context)

def hospitalsubject(request):
    selected_subject = request.GET.getlist('rad_sub')
    print(selected_subject)

    data = jsondecode()

    context={
        'selected_locations': request.session['selected_locations'],
        'data':data,
        'subjects':subjects,
        'selected_subject':selected_subject,
    }
    return render(request, 'main/hospitalsubject.html', context)

def hospitaldetail(request, name):
    try:
        # 병원api
        url = f'https://open.jejudatahub.net/api/proxy/tbb1D1a1559at91ababaata1abtba58a/{your_appkey}?openStatus={status}&bizSmallType={bizSmallType}&companyName={name}'

        response = requests.get(url)
        data = response.json()

        # 데이터가 종종 update날짜만 다른 2개 이상인 값이 있음 ex) 서귀포열린병원
        # update 날짜가 최신인 것만 취급
        data2 = sorted(data['data'], key=lambda x: x['updateAt'], reverse=True)
        data['data'] = data2

        # 저장후 불러오기
        hospital_reples = Review.objects.filter(companyName=name)
        total_star = Review.objects.filter(companyName=name).aggregate(Avg('star'))

        context={
            'data':data,
            'hospital_reples':hospital_reples,
            'total_star':total_star,
        }
        return render(request,'main/hospitaldetail.html',context)
    except json.JSONDecodeError as e:
        raise Http404('페이지를 찾을 수 없습니다. 새로고침을 시도해주세요.')



def comment(request):
    jsonOject = json.loads(request.body)

    companyName=jsonOject.get('companyName')
    

    # db에 저장
    reple = Review.objects.create(
        #user_id=jsonOject.get('user_id'),
        user_id=User.objects.get(user_id=jsonOject.get('user_id')), # user_id는 User테이블을 참조하는 FK키
        title=jsonOject.get('title'),
        content=jsonOject.get('content'),
        star=jsonOject.get('star'),
        companyName=jsonOject.get('companyName'),
        licenseDate=jsonOject.get('licenseDate'),
    )

    return redirect('hospitaldetail', name=companyName)
