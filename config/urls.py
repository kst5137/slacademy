"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import board.views
import ex01.views
import comment.views
import users.views

urlpatterns = [
    path('admin/', admin.site.urls),
    #     패스함수를 통해 admin/를 admin.site.urls와 연결

    path('ex01/func1', ex01.views.func1),
    path('ex01/func2', ex01.views.func2),
    path('ex01/func3', ex01.views.func3),

    # board 관련
    path('board/register',board.views.register),
    path('board/list',board.views.posts),
    path('board/read/<int:bid>', board.views.read),
    # <> 안에는 숫자를 넣는데 bid에 숫자를 넣는다.
    path('board/delete/<int:bid>', board.views.delete),
    path('board/update/<int:bid>', board.views.update),
    path('', board.views.home),
    path('board/test', board.views.test),

    # Q01 comment로 만들어보기
    path('comment/register',comment.views.register),
    path('comment/list',comment.views.posts),
    path('comment/read/<int:bid>', comment.views.read),
    # <> 안에는 숫자를 넣는데 bid에 숫자를 넣는다.
    path('comment/delete/<int:bid>', comment.views.delete),
    path('comment/update/<int:bid>', comment.views.update),

    # q02 users 만들어보기
    path('users/signup2',users.views.signup),
    path('users/login',users.views.userlogin),
    path('users/logout', users.views.userlogout),

    # #api연습
    # path('api',board.views.api),
    # path('ajax',board.views.ajax),

    path('board/like/<int:bid>', board.views.like),



    #ex01/func1의 uri와 ex01이라는 폴더안에 views라는 파일의 func1을 찾아간거
    #그래서 도메인에 127.0.0.1:8000/ex01/func1을 하면 func1이 만들어진게 보여지는것
]
