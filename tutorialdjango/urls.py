from django.contrib import admin
from django.urls import path, include
from main.views import index, login, logout, user_regist,comment, hospitaldetail, hospitallist, hospitalsubject
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),

    # 로그인
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('user_regist/', user_regist, name='user_regist'),

    # 병원 찾기
    path('hospitallist/', hospitallist, name='hospitallist'),
    path('hospitalsubject/',hospitalsubject, name='hospitalsubject'),
    path('hospitaldetail/<str:name>', hospitaldetail, name='hospitaldetail'),
    
    # 후기
    path('comment/', comment, name='comment'),
]

urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)