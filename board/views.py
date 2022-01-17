from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from board.forms import BoardForm
from board.models import Board


@login_required(login_url='/user/login')
def register(request):
    if request.method == "GET":
        boardForm = BoardForm()  # 입력칸에 아무것도 없는 상태로 준다
        return render(request, 'board/test.html',
                      {'boardForm': boardForm})
    # render라는 함수가 boardForm의 데이터 board폴더에 forms.py 안에 있는 데이터  받아와 board/register3.html을 완성시킨다는 개념

    elif request.method == "POST":
        boardForm = BoardForm(request.POST)
        # 모델폼을 이용하면 알아서 다 받아짐
        if boardForm.is_valid():  # boardForm안에 값이 유효한다면
            board = boardForm.save(commit=False)
            board.writer = request.user
            board.save()
            return redirect('/board/list')


def posts(request):
    posts = Board.objects.all()  # board table에서 모든 데이터를 다 가져옴

    return render(request, 'board/list.html',
                  {'posts': posts})


def read(request, bid):
    post = Board.objects.get(Q(id=bid))  # bid에 해당하는 내용이 post에 담기고
    # sql에서 where라는 조건 지정한것처럼 조건을 지정한다.
    # 게시글의 id를 불러올 것이다
    # bid는 사용자가 누른 게시글에 대한 얘기
    return render(request, 'board/read.html', {'read': post})


@login_required(login_url='/user/login')
def delete(request, bid):
    post = Board.objects.get(Q(id=bid))
    if request.user != post.writer:
        return render(request, 'board/list.html')
    post.delete()
    return redirect('/board/list')


# 수정은 게시글 조회와 작성을 한번에 보여줘야해서 가장 어려움


@login_required(login_url='/user/login')
def update(request, bid):
    post = Board.objects.get(Q(id=bid))  # 게시글 하나를 가져오는것
    if request.user != post.writer:
        return render(request, 'board/list.html')
    post.delete()
    if request.method == "GET":
        # boardForm = BoardForm()      #입력칸에 아무것도 없는 상태로 준다
        boardForm = BoardForm(instance=post)  # 입력칸에 아무것도 없는 상태로 준다
        return render(request, 'board/update.html', {'boardForm': boardForm})
    elif request.method == "POST":
        boardForm = BoardForm(request.POST)
        # boardForm에서 사용자가 보내온 데이터를 받느다
        if boardForm.is_valid():  # boardForm안에 값이 유효한다면
            post.title = boardForm.cleaned_data['title']
            post.contents = boardForm.cleaned_data['contents']
            post.save()
            # return redirect('/board/read/' + str(bid))
            return redirect('/board/list')


def signup(request):
    if request.method == "GET":
        signupForm = UserCreationForm()
        return render(request, 'users/signup.html', {'signupForm': signupForm})

    elif request.method == "POST":
        signupForm = UserCreationForm(request.POST)
        if signupForm.is_valid():
            signupForm.save()
            return redirect('/users/signup')


def userlogin(request):
    if request.method == "GET":
        loginForm = AuthenticationForm()
        return render(request, 'users/login.html', {'loginForm': loginForm})
    elif request.method == "POST":
        loginForm = AuthenticationForm(request, request.POST)
        if loginForm.is_valid():  # 검증단계
            login(request, loginForm.get_user())
            return redirect('/board/list')
        else:
            return redirect('/users/login')


def userlogout(request):
    logout(request)
    return redirect('/users/login')


def home(request):
    return render(request, 'layout/base.html')


def test(request):
    return render(request, 'board/test.html')


@login_required(login_url='/user/login')
def like(request, bid):
    post = Board.objects.get(Q(id=bid)) # 게시글 번호를 불러오고
    user = request.user
    if post.like.filter(id=user.id).exists():  # 필터로 그 게시글 번호에 특정 id의 사용자가 누른 좋아요가 있으면
        post.like.remove(user)
        message = 'del'
    else:
        post.like.add(user)  # 게시글 좋아요 아직 안눌렀음
        message = 'add'
    return JsonResponse(
        {
            'message': message,
            'like_cnt': post.like.count()
        }
    )

# # api 연습
# def api(request) :
#     json = {'key1': 'value1', 'key2': 'value2'}
#     response = JsonResponse(json, safe=False)  # ()안에 데이터를 담아서 보낸다
#     # safe False는 우리 서버가 아닌 다른 서버에 보낼때 url을 맞춰줘야 하는데 그런 기능 보안 점검기능을 잠시 끄는것
#     return response
#
#
# def ajax(request) :
#     return render(request, 'ajax.html')
